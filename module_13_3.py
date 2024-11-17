# Цель: написать простейшего телеграм-бота, используя асинхронные функции.

# Задача "Он мне ответил!":

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio

API_TOKEN = ""

# Создаем объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработка команды /start
@dp.message_handler(commands=["start"])
async def start(message: Message):
    # Асинхронный вызов метода answer для отправки сообщения
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")

# Обработка всех остальных сообщений
@dp.message_handler()
async def all_messages(message: Message):
    # Асинхронный вызов метода answer для отправки ответа
    await message.answer("Введите команду /start, чтобы начать общение.")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)


