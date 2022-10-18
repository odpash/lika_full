from aiogram import types
from aiogram.dispatcher import FSMContext

from app.database.db import write_to_db
from app.handlers.frequent_cases import welcome_command
from app.utils import buttons
from app.utils.states import Add
from app.utils import messages
from app.main import dp

EVIASFORM = "https://evisaforms.state.gov/"


@dp.message_handler(lambda m: m.text == buttons.add_new_account_btn.text)
async def add_site(message: types.Message):
    await message.reply(messages.INPUT_SITE, reply_markup=buttons.sites)
    await Add.site.set()


@dp.message_handler(state=Add.site)
async def add_login(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["site"] = message.text

    if message.text == EVIASFORM:
        await message.reply(messages.INPUT_COUNTRY, reply_markup=buttons.none)
        await Add.country.set()
    else:
        await message.reply(messages.INPUT_LOGIN, reply_markup=buttons.none)
        await Add.login.set()


@dp.message_handler(state=Add.login)
async def add_password(message: types.Message, state: FSMContext):
    await message.reply(messages.INPUT_PASSWORD, reply_markup=buttons.none)
    async with state.proxy() as data:
        data["login"] = message.text
    await Add.password.set()


# if site https://evisaforms.state.gov/
@dp.message_handler(state=Add.country)
async def add_country(message: types.Message, state: FSMContext):
    await message.reply(messages.INPUT_PATCH, reply_markup=buttons.none)
    async with state.proxy() as data:
        data["country"] = message.text
    await Add.patch.set()


@dp.message_handler(state=Add.patch)
async def add_patch(message: types.Message, state: FSMContext):
    await message.reply(messages.INPUT_NUMBER_OF_APPLICATION, reply_markup=buttons.none)
    async with state.proxy() as data:
        data["patch"] = message.text
    await Add.number_of_application.set()


@dp.message_handler(state=Add.number_of_application)
async def add_number_of_application(message: types.Message, state: FSMContext):
    await message.reply(messages.INPUT_NO_LATER_THAN, reply_markup=buttons.skip)
    async with state.proxy() as data:
        data["number_of_application"] = message.text
    await Add.no_later_than.set()


# END of if site https://evisaforms.state.gov/


@dp.message_handler(state=Add.password)
async def add_no_later_than(message: types.Message, state: FSMContext):
    await message.reply(messages.INPUT_NO_LATER_THAN, reply_markup=buttons.skip)
    async with state.proxy() as data:
        data["password"] = message.text
    await Add.no_later_than.set()


@dp.message_handler(state=Add.no_later_than)
async def add_remove_dates(message: types.Message, state: FSMContext):
    await message.reply(messages.INPUT_REMOVE_DATES, reply_markup=buttons.skip)
    async with state.proxy() as data:
        data["no_later_than"] = message.text
    await Add.remove_dates.set()


@dp.message_handler(state=Add.remove_dates)
async def add_no_less_than(message: types.Message, state: FSMContext):
    await message.reply(messages.INPUT_NO_LESS_THAN, reply_markup=buttons.skip)
    async with state.proxy() as data:
        data["remove_dates"] = message.text
    await Add.no_less_than.set()


@dp.message_handler(state=Add.no_less_than)
async def add_account(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["no_less_than"] = message.text
        information = data.as_dict()
        await write_to_db(information)
    await state.finish()
    await message.reply(
        messages.ADD_APPROVED, parse_mode="html", reply_markup=buttons.none
    )
    await welcome_command(message)
