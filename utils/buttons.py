from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


# HELLO START
show_all_accounts_btn = KeyboardButton("Показать все аккаунты")
add_new_account_btn = KeyboardButton("Добавить новый аккаунт")
delete_account_btn = KeyboardButton("Удалить аккаунт по id")
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(show_all_accounts_btn)
menu.add(add_new_account_btn)
menu.add(delete_account_btn)
# HELLO END


# CREATE ACCOUNT
none = ReplyKeyboardRemove()
sites = ReplyKeyboardMarkup(resize_keyboard=True)
sites.add("https://cgifederal.secure.force.com/")
sites.add("https://ais.usvisa-info.com/")
sites.add("https://evisaforms.state.gov/")
skip = ReplyKeyboardMarkup(resize_keyboard=True)
skip.add("Пропустить")
