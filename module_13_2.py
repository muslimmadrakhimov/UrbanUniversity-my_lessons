

# Цель: написать простейшего телеграм-бота, используя асинхронные функции.


# Импортируем необходимые библиотеки из aiogram
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = ""

# Настройка бота и диспетчера
bot = Bot(token=API_TOKEN)  # Объект бота, который связывается с Telegram API
dp = Dispatcher(bot)  # Диспетчер, который управляет обработкой сообщений

# Функция для обработки команды /start
@dp.message_handler(commands=['start'])  # Эта функция сработает при получении команды /start
async def start(message: types.Message):
    """
    Эта функция отвечает на команду /start.
    При получении команды /start бот отправит пользователю сообщение
    и выведет текст в консоль.
    """
    print("Привет! Я бот помогающий твоему здоровью.")  # Выводим в консоль приветствие
    await message.reply("Привет! Я бот помогающий твоему здоровью.")  # Отправляем пользователю сообщение

# Функция для обработки всех остальных сообщений
@dp.message_handler()  # Эта функция сработает для любых сообщений, не являющихся командой /start
async def all_messages(message: types.Message):
    """
    Эта функция отвечает на любые сообщения, кроме команды /start.
    Бот напомнит пользователю использовать команду /start.
    """
    print("Введите команду /start, чтобы начать общение.")  # Выводим в консоль напоминание
    await message.reply("Введите команду /start, чтобы начать общение.")  # Отправляем ответ в чат

# Главная функция, которая запускает бота
if __name__ == "__main__":
    """
    В этой части программы запускается polling (опрос) сообщений, 
    чтобы бот мог постоянно получать новые сообщения.
    """
    print("Bot is running...")  # Выводим в консоль сообщение о запуске бота
    executor.start_polling(dp, skip_updates=True)  # Запускаем polling, чтобы бот мог получать новые сообщения
