from aiogram.dispatcher.filters.state import StatesGroup, State


class Add(StatesGroup):
    site = State()
    login = State()
    password = State()
    no_later_than = State()
    remove_dates = State()
    no_less_than = State()
    country = State()
    patch = State()
    number_of_application = State()


class Remove(StatesGroup):
    is_active = State()
