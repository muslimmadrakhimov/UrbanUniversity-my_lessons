# Цель: научится создавать клавиатуры и кнопки на них в Telegram-bot.

# Задача "Меньше текста, больше кликов":



from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor


API_TOKEN = ''

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Класс состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Клавиатура для команды /start
start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard.add(KeyboardButton("Рассчитать"), KeyboardButton("Информация"))


# Хэндлер для команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот, помогающий твоему здоровью.",
        reply_markup=start_keyboard
    )


# Хэндлер для кнопки "Информация"
@dp.message_handler(lambda message: message.text == "Информация")
async def info(message: types.Message):
    await message.answer(
        "Я бот, который рассчитывает вашу норму калорий на основе возраста, роста и веса. "
        "Нажмите 'Рассчитать', чтобы начать процесс!"
    )


# Хэндлер для кнопки "Рассчитать" — Начало машины состояний
@dp.message_handler(lambda message: message.text == "Рассчитать")
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


# Хэндлер для ввода возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or int(message.text) <= 0:
        await message.answer("Возраст должен быть положительным числом. Попробуйте снова:")
        return
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост (в сантиметрах):")
    await UserState.growth.set()


# Хэндлер для ввода роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or int(message.text) <= 0:
        await message.answer("Рост должен быть положительным числом. Попробуйте снова:")
        return
    await state.update_data(growth=int(message.text))
    await message.answer("Введите свой вес (в килограммах):")
    await UserState.weight.set()


# Хэндлер для ввода веса
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if not message.text.isdigit() or int(message.text) <= 0:
        await message.answer("Вес должен быть положительным числом. Попробуйте снова:")
        return
    await state.update_data(weight=int(message.text))

    # Получение данных пользователя
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Расчёт нормы калорий (Миффлин — Сан Жеор для мужчин)
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories:.2f}")
    await state.finish()


# Хэндлер по умолчанию для любых других сообщений
@dp.message_handler()
async def handle_unknown(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
