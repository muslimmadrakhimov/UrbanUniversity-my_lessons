# Цель: получить навык работы с состояниями в телеграм-боте.
# Задача "Цепочка вопросов":


from aiogram import Bot, Dispatcher, types  # Основные компоненты для работы с ботом
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # Хранилище для состояний
from aiogram.dispatcher import FSMContext  # Контекст состояний
from aiogram.dispatcher.filters.state import State, StatesGroup  # Классы для описания состояний
from aiogram.utils import executor  # Модуль для запуска бота

# Шаг 1: Создаём экземпляр бота и диспетчера
API_TOKEN = ''
bot = Bot(token=API_TOKEN)  # Инициализация бота
storage = MemoryStorage()  # Хранилище состояний (в оперативной памяти)
dp = Dispatcher(bot, storage=storage)  # Диспетчер для обработки сообщений

# Шаг 2: Создаём группу состояний
class UserState(StatesGroup):
    """
    Группа состояний для последовательного запроса данных:
    - Возраст (age)
    - Рост (growth)
    - Вес (weight)
    """
    age = State()      # Ввод возраста
    growth = State()   # Ввод роста
    weight = State()   # Ввод веса

# Шаг 3: Обработка команды /start
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    """
    Приветственное сообщение при вводе команды /start.
    """
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

# Шаг 4: Обработка команды 'Calories' — начало диалога
@dp.message_handler(lambda message: message.text == 'Calories')  # Если сообщение == 'Calories'
async def set_age(message: types.Message):
    """
    Запускаем цепочку запроса данных с вопроса про возраст.
    """
    await message.answer("Введите свой возраст:")  # Просим ввести возраст
    await UserState.age.set()  # Устанавливаем текущее состояние как age

# Шаг 5: Ввод возраста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    """
    Получаем возраст пользователя, сохраняем его и переходим к следующему шагу — рост.
    """
    age = int(message.text)  # Преобразуем ввод в число
    await state.update_data(age=age)  # Сохраняем возраст в состояние
    await message.answer("Введите свой рост (в см):")  # Просим ввести рост
    await UserState.growth.set()  # Устанавливаем текущее состояние как growth

# Шаг 6: Ввод роста
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    """
    Получаем рост пользователя, сохраняем его и переходим к следующему шагу — вес.
    """
    growth = int(message.text)  # Преобразуем ввод в число
    await state.update_data(growth=growth)  # Сохраняем рост в состояние
    await message.answer("Введите свой вес (в кг):")  # Просим ввести вес
    await UserState.weight.set()  # Устанавливаем текущее состояние как weight

# Шаг 7: Ввод веса и подсчёт калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    """
    Получаем вес, вычисляем норму калорий и отправляем результат.
    """
    weight = int(message.text)  # Преобразуем ввод в число
    await state.update_data(weight=weight)  # Сохраняем вес в состояние

    # Получаем все данные из состояния
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Формула Миффлина - Сан Жеора для мужчин:
    # Калории = 10 * вес + 6.25 * рост - 5 * возраст + 5
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    # Отправляем результат
    await message.answer(f"Ваша норма калорий: {calories:.2f}")

    # Завершаем цепочку
    await state.finish()

# Шаг 8: Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
