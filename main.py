import json, string
from aiogram import Bot, types, Dispatcher
from aiogram import types


# Создаем переменную бота
bot = Bot(token="BOT TOKKEN FROM @BotFather", parse_mode=types.ParseMode.HTML)

# Создаем диспетчер
dp = Dispatcher(bot)

__all__ = ['bot']


@dp.message_handler()
async def censor_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Не материмся!!!')
        await message.delete()

