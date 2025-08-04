from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter,CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import csv

from filters.chat_types import ChatTypeFilter
from kbds.reply import get_keyboard

registration_router = Router()

class Add_user(StatesGroup):
    #Шаги состояний
    name = State()
    wilbrs_kart_id = State()


# FSM
@registration_router.message(StateFilter(None),CommandStart())
async def start_registration(message:types.Message,state:FSMContext):
    await message.answer(
        "start registration:\n\nВведите своё имя: ", reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(Add_user.name)

@registration_router.message(Add_user.name, F.text)
async def add_name(message: types.Message, state: FSMContext):
        await state.update_data(name=message.text)
        await message.answer('Введите id карты')
        await state.set_state(Add_user.wilbrs_kart_id)

@registration_router.message(Add_user.name)
async def add_name2(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели не допустимые данные, введите команду /start")

@registration_router.message(Add_user.wilbrs_kart_id, F.text)
async def add_description(message: types.Message, state: FSMContext):
    await state.update_data(wilbrs_kart_id=message.text)
    await message.answer("user добавлен")
    data = await state.get_data()
    await state.set_state(Add_user.wilbrs_kart_id)
    await message.answer(str(data))
    print(type(data))
    await state.clear()
    with open('users.csv','w') as file:
        fieldnames = ['name','wilbrs_kart_id']

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Записываем заголовки
        writer.writerow(data)
