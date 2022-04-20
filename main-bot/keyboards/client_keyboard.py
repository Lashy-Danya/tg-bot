from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

keyboard_client = ReplyKeyboardMarkup(resize_keyboard = True)

button_1 = KeyboardButton('/help')
keyboard_client.add(button_1)

