from aiogram import F, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import (
    as_list,
    as_marked_section,
    Bold,
)  # Italic, as_numbered_list и тд

from filters.chat_types import ChatTypeFilter

from kbds.reply import get_keyboard

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


# @user_private_router.message(CommandStart())
# async def start_cmd(message: types.Message):
#     await message.answer(
#         "Привет, я виртуальный помощник",
#         reply_markup=get_keyboard(
#             'Реклама',
#             placeholder="Что вас интересует?",
#         ),
#     )


@user_private_router.message((F.text.lower() == "реклама"))
async def menu_cmd(message: types.Message):
    await message.answer("возможные функции: ",
                         reply_markup=get_keyboard(
                             'ручное управление',
                             'статистика',
                             'автоматическое управление',
                             sizes=(2,1)
                         ),
                    )


@user_private_router.message(F.text.lower() == 'ручное управление')
async def start_cmd(message: types.Message):
    await message.answer(
        "возможные функции: ",
        reply_markup=get_keyboard(
            "f1",
            "f2",
            "f3"
        ),
    )


@user_private_router.message(F.text.lower() == 'статистика')
async def start_cmd(message: types.Message):
    await message.answer(
        "возможные функции: ",
        reply_markup=get_keyboard(
            "s1",
            "s2"
        ),
    )

@user_private_router.message(F.text.lower() == 'автоматическое управление')
async def start_cmd(message: types.Message):
    await message.answer(
        "возможные функции: ",
        reply_markup=get_keyboard(
            "a1",
            "a2"
        ),
    )


# @user_private_router.message(F.contact)
# async def get_contact(message: types.Message):
#     await message.answer(f"номер получен")
#     await message.answer(str(message.contact))


# @user_private_router.message(F.location)
# async def get_location(message: types.Message):
#     await message.answer(f"локация получена")
#     await message.answer(str(message.location))
