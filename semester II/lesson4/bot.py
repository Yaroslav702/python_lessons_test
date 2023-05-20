import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.builtin import CommandStart
from dotenv import load_dotenv


load_dotenv()

TOKEN=os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(CommandStart())
async def start(message: types.Message):
    await message.answer(text='Echo bot')


@dp.message_handler(text='Hello')
async def greetings(message: types.Message):
    name = message.from_user.full_name
    await message.answer(f'Hello {name}.\nMy name is Geralt.')


@dp.message_handler(commands=['info'])
async def user_info(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    telegram_id = message.from_id
    lang = message.from_user.language_code

    await message.answer(f'ID: {telegram_id}\nFIRST_NAME: {first_name}\nLAST_NAME: {last_name}\nUSERNAME: @{username}\nLANGUAGE: {lang}')

@dp.message_handler(content_types='text')
async def echo(message: types.Message):
    if message.text == 'Weather':
        await message.answer('bebebe')
    else:
        await message.answer(text=f'PC: {message.text}')


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def echo_sticker(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)






if __name__ == '__main__':
    executor.start_polling(dp)