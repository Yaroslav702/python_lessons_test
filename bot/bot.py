import logging

from aiogram import Bot, Dispatcher, executor, types

from keyboards import *
from films import FILMS

TOKEN='6103082934:AAEn9v6Y3SYmgTGk-b4UYrN7n2b2ZA4hBsI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(text='Привіт! Я - бот-кіноафіша. Обери фільм, про який ти хочеш дізнатися.', reply_markup=film_choice)


@dp.callback_query_handler()
async def get_film_info(callback_query: types.CallbackQuery):
    if callback_query.data == 'Джон Уік 4 (16+)':
        await bot.send_photo(callback_query.message.chat.id, FILMS[callback_query.data]["photo"])
        url= FILMS[callback_query.data]["site_url"]
        film_rating = FILMS[callback_query.data]["rating"]
        film_description = FILMS[callback_query.data]["description"]
        message = f"<b>Film url:</b> {url}\n<b>About:</b> {film_description}\n\n<b>Rate:</b> {film_rating}"
        await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')
    elif callback_query.data == 'Підземелля і дракони':
        await bot.send_photo(callback_query.message.chat.id, FILMS[callback_query.data]["photo"])
        url= FILMS[callback_query.data]["site_url"]
        film_rating = FILMS[callback_query.data]["rating"]
        film_description = FILMS[callback_query.data]["description"]
        message = f"<b>Film url:</b> {url}\n<b>About:</b> {film_description}\n\n<b>Rate:</b> {film_rating}"
        await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')
    elif callback_query.data == 'Екзорцист Ватикану':
        await bot.send_photo(callback_query.message.chat.id, FILMS[callback_query.data]["photo"])
        url= FILMS[callback_query.data]["site_url"]
        film_rating = FILMS[callback_query.data]["rating"]
        film_description = FILMS[callback_query.data]["description"]
        message = f"<b>Film url:</b> {url}\n<b>About:</b> {film_description}\n\n<b>Rate:</b> {film_rating}"
        await bot.send_message(callback_query.message.chat.id, message, parse_mode='html')

# @dp.message_handler()
# async def echo(message: types.Message):
#     user_info = {
#         "name": message.from_user.first_name,
#         "surname": message.from_user.last_name,
#         "username": message.from_user.username,
#         "user_id": message.from_user.id
#     }
#     await message.answer(f'First name: {user_info["name"]}\nLast name: {user_info["surname"]}\nUsername: {user_info["username"]}\nUser id: {user_info["user_id"]}')
#     await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp)