from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


film_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Джон Уік 4 (16+)", callback_data="Джон Уік 4 (16+)")],
        [InlineKeyboardButton(text="Підземелля і дракони", callback_data="Підземелля і дракони")],
        [InlineKeyboardButton(text="Екзорцист Ватикану", callback_data="Екзорцист Ватикану")]
    ]
)