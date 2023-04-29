from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from films import films

film_choice = InlineKeyboardMarkup()
for film in films:
    button = InlineKeyboardButton(text=film, callback_data=film)
    film_choice.add(button)

shops = ['Adidas', 'H&M']

shop_choice = InlineKeyboardMarkup()
for shop in shops:
    button = InlineKeyboardButton(text=shop, callback_data=shop)
    shop_choice.add(button)


# [InlineKeyboardButton(text="Джон Уік 4 (16+)", callback_data="Джон Уік 4 (16+)")],
# [InlineKeyboardButton(text="Підземелля і дракони", callback_data="Підземелля і дракони")],
# [InlineKeyboardButton(text="Екзорцист Ватикану", callback_data="Екзорцист Ватикану")]





if __name__ == '__main__':
    dictionary = {
    1: 'ONE',
    2: 'TWO'
    } 

    for key, value in dictionary.items():
        print(key, value)