#Цель: подготовить Telegram-бота для взаимодействия с базой данных.

#Задача "Витамины для всех!":





# Импортируем необходимые модули из библиотеки aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Хранилище состояний в оперативной памяти
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup  # Для работы с состояниями пользователя
from aiogram.dispatcher import FSMContext  # Контекст состояний для передачи данных между шагами

# 1. Token bot
API_TOKEN = ''

# 2. Создаём экземпляры бота, хранилища и диспетчера
bot = Bot(token=API_TOKEN)  # Создаём объект бота
storage = MemoryStorage()  # Создаём объект для хранения временных данных
dp = Dispatcher(bot, storage=storage)  # Связываем бота и хранилище с диспетчером

# 3. Создаём клавиатуры для взаимодействия с пользователем

# Главная клавиатура (обычная) с большими кнопками внизу чата
main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],  # Кнопка для запуска расчёта калорий
        [KeyboardButton(text='Информация')],  # Кнопка для получения справочной информации
        [KeyboardButton(text='Купить')]  # Новая кнопка для покупки товаров
    ],
    resize_keyboard=True  # Подгоняем размер кнопок под размер экрана
)

# Инлайн-клавиатура (встраивается в сообщение) для выбора продуктов
inline_products_kb = InlineKeyboardMarkup(row_width=2)  # Указываем, что в строке будет 2 кнопки
inline_products_kb.add(
    InlineKeyboardButton(text='Product1', callback_data='product_buying'),  # Первая кнопка
    InlineKeyboardButton(text='Product2', callback_data='product_buying'),  # Вторая кнопка
    InlineKeyboardButton(text='Product3', callback_data='product_buying'),  # Третья кнопка
    InlineKeyboardButton(text='Product4', callback_data='product_buying')  # Четвёртая кнопка
)


# 4. Обработчики команд и кнопок

# Обработчик команды /start - запускается, когда пользователь вводит /start в чате
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Отправляем приветственное сообщение и показываем главное меню
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=main_menu_kb)


# Обработчик нажатия кнопки "Купить" в главном меню
@dp.message_handler(lambda message: message.text == 'Купить')  # Срабатывает, если пользователь нажал "Купить"
async def get_buying_list(message: types.Message):
    # Путь к изображениям продуктов
    product_file_ids = [
        "files/image1.jpeg",  # Путь для Product1
        "files/image2.jpeg",  # Путь для Product2
        "files/image3.jpeg",  # Путь для Product3
        "files/image4.jpeg"  # Путь для Product4
    ]

    # Названия, описания и цены продуктов
    product_names = [
        "Product1",
        "Product2",
        "Product3",
        "Product4"
    ]

    product_descriptions = [
        "Описание 1",
        "Описание 2",
        "Описание 3",
        "Описание 4"
    ]

    product_prices = [
        100,  # Цена продукта в рублях
        200,  # Цена продукта в рублях
        300,  # Цена продукта в рублях
        400  # Цена продукта в рублях
    ]

    # Отправляем информацию о продуктах: название, описание и цена
    for i in range(4):
        # Формируем текст для каждого продукта
        product_text = f"Название: {product_names[i]} | Описание: {product_descriptions[i]} | Цена: {product_prices[i]} руб."

        # Отправляем текст
        await message.answer(product_text)

        # Открываем и отправляем изображение
        with open(product_file_ids[i], "rb") as photo:
            await message.answer_photo(
                photo=photo
            )

    # После описания всех продуктов выводим инлайн-клавиатуру для выбора
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_products_kb)


# Обработчик нажатия кнопок инлайн-меню (выбор продукта)
@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    # Отправляем сообщение о том, что продукт успешно куплен
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()  # Закрываем "часики" на кнопке (чтобы не крутилось)


# 5. Запуск бота
if __name__ == '__main__':
    # Стартуем процесс получения обновлений и обработки сообщений
    executor.start_polling(dp,
                           skip_updates=True)  # skip_updates пропускает старые сообщения, полученные до запуска бота
