# Цель: научится создавать Inline клавиатуры и кнопки на них в Telegram-bot.

# Задача "Ещё больше выбора":


from aiogram import Bot, Dispatcher, executor, types  # Основные модули Aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Для хранения состояний в памяти
from aiogram.dispatcher.filters.state import State, StatesGroup  # Для работы с состояниями
from aiogram.dispatcher import FSMContext  # Для работы с контекстом состояний (передача данных между шагами)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# 1.
API_TOKEN = ''

# 2. Настраиваем бота, диспетчер и хранилище состояний.
bot = Bot(token=API_TOKEN)  # Инициализация бота
storage = MemoryStorage()  # Хранилище состояний в оперативной памяти
dp = Dispatcher(bot, storage=storage)  # Связываем бота и хранилище с диспетчером

# 3. Определяем класс состояний, через которые будет проходить пользователь.
class CalcStates(StatesGroup):
    waiting_for_age = State()  # Состояние ожидания ввода возраста
    waiting_for_height = State()  # Состояние ожидания ввода роста
    waiting_for_weight = State()  # Состояние ожидания ввода веса

# 4. Создаём клавиатуры (меню) для общения с пользователем.

# Главное меню (ReplyKeyboardMarkup) - это меню внизу чата с двумя большими кнопками
main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],  # Кнопка для начала расчёта
        [KeyboardButton(text='Информация')]  # Кнопка для получения информации
    ],
    resize_keyboard=True  # Подгоняем размер кнопок под экран
)

# Инлайн-клавиатура (InlineKeyboardMarkup) - это кнопки прямо внутри сообщений
inline_menu_kb = InlineKeyboardMarkup(row_width=2)  # Количество кнопок в строке
inline_menu_kb.add(
    InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
    InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
)

# 5. Обработчики команд и кнопок

# Обработчик команды /start - приветствие пользователя
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Приветственное сообщение с главным меню
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=main_menu_kb)

# Обработчик нажатия кнопки "Рассчитать" в главном меню
@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    # Сообщение с инлайн-кнопками
    await message.answer("Выберите опцию:", reply_markup=inline_menu_kb)

# Обработчик нажатия кнопки "Формулы расчёта"
@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    # Отправляем сообщение с формулой расчёта калорий
    formula = (
        "10 × вес (кг) + 6,25 × рост (см) − 5 × возраст (годы) − 161 (для женщин)\n"
        "10 × вес (кг) + 6,25 × рост (см) − 5 × возраст (годы) + 5 (для мужчин)"
    )
    await call.message.answer(formula)
    await call.answer()  # Закрываем "часики" на кнопке

# Обработчик нажатия кнопки "Рассчитать норму калорий"
@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    # Запускаем процесс: сначала спрашиваем возраст
    await call.message.answer("Введите свой возраст:")
    await CalcStates.waiting_for_age.set()  # Устанавливаем состояние "ожидание возраста"
    await call.answer()  # Закрываем "часики" на кнопке

# Шаг 1. Получаем возраст
@dp.message_handler(state=CalcStates.waiting_for_age)
async def process_age(message: types.Message, state: FSMContext):
    # Получаем возраст и сохраняем его во временное хранилище (FSMContext)
    age = int(message.text)  # Преобразуем текст в число
    await state.update_data(age=age)  # Сохраняем возраст
    await message.answer("Введите свой рост (в сантиметрах):")
    await CalcStates.waiting_for_height.set()  # Переходим к следующему состоянию

# Шаг 2. Получаем рост
@dp.message_handler(state=CalcStates.waiting_for_height)
async def process_height(message: types.Message, state: FSMContext):
    # Получаем рост и сохраняем его
    height = int(message.text)
    await state.update_data(height=height)  # Сохраняем рост
    await message.answer("Введите свой вес (в килограммах):")
    await CalcStates.waiting_for_weight.set()  # Переходим к следующему состоянию

# Шаг 3. Получаем вес и рассчитываем калории
@dp.message_handler(state=CalcStates.waiting_for_weight)
async def process_weight(message: types.Message, state: FSMContext):
    # Получаем вес
    weight = int(message.text)
    await state.update_data(weight=weight)  # Сохраняем вес

    # Извлекаем все данные (возраст, рост, вес) из хранилища
    user_data = await state.get_data()
    age = user_data['age']
    height = user_data['height']

    # Расчёт нормы калорий по формуле для женщин
    calories = 10 * weight + 6.25 * height - 5 * age - 161

    # Отправляем результат
    await message.answer(f"Ваша норма калорий: {calories:.1f}")

    # Сбрасываем состояние (завершаем процесс)
    await state.finish()

# 6. Запуск бота
if __name__ == '__main__':
    # Запускаем бот и пропускаем обновления, которые пришли, пока бот был выключен
    executor.start_polling(dp, skip_updates=True)
