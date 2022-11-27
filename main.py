import logging

import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

API_TOKEN = '5633696871:AAERFSkxagmHcBG8Yl6Ed5VgeaRGDV9UeDo'

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    ish = State()
    ism = State()
    t_yil = State()
    manzil = State()
    numer = State()
    til = State()
    oylik = State()

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Kassir", "Adminstrator", "Oshpaz Yordamchi", "Ofitsant", "Dasturxonchi", "Tozalik Xodimi", "Idish Yuvuvchi")
    await Form.ish.set()
    await message.reply("Salom Mumtoz HR Botiga Xush Kelibsiz\n\nBo'sh Ish O'rnini Tanlang 👇🏻", reply_markup=markup)

@dp.message_handler(commands='help')
async def help_start(message: types.Message):
    await message.reply("Bu Bot Orqali Siz Mumtoz Restoranidagi Bo'sh Ish O'rinlariga Ariza Qoldirishingiz Mumkin\n\nBotni Ishga Tushurish Uchun /start deb Yozing!")

@dp.message_handler(state=Form.ish)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ish'] = message.text

    await Form.next()
    await message.reply("F.I.Sh Kiriting\nMasalan: XOJIYEV ISMOIL")

@dp.message_handler(lambda message: not message.text.isupper(), state=Form.ism)
async def process_name_invalid(message: types.Message):
    return await message.reply("Xatolik Malumotni To'g'ri Kiriting")

@dp.message_handler(state=Form.ism)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ism'] = message.text
    await Form.next()
    await message.reply("Tug'ulgan Yilingizni Kiriting\nMasalan: 2006")


@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.t_yil)
async def process_age_invalid(message: types.Message):
    return await message.reply("Xatolik Malumotni To'g'ri Kiriting")

@dp.message_handler(lambda message: message.text.isdigit(), state=Form.t_yil)
async def process_age(message: types.Message, state: FSMContext):
    await Form.next()
    await state.update_data(t_yil=int(message.text))
    await message.reply("Yashash Manzilingizni Kiriting\nMasalan: TOSHKENT ANGREN")

@dp.message_handler(lambda message: not message.text.isupper(), state=Form.manzil)
async def process_name_invalid(message: types.Message):
    return await message.reply("Xatolik Malumotni To'g'ri Kiriting")

@dp.message_handler(state=Form.manzil)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['manzil'] = message.text

    await Form.next()
    await message.reply("Telefon Raqamingizni Kiriting\nMasalan: 930382606")

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.numer)
async def process_age_invalid(message: types.Message):
    return await message.reply("Xatolik Malumotni To'g'ri Kiriting Hech Qanday Qo'shimchalarsiz")

@dp.message_handler(state=Form.numer)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['numer'] = message.text

    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup2.add("Bilmayman Gaplasha Olmayman", "Tushunaman Gaplasha Olmayman", "Tushunaman Gaplasha Olaman")
    await Form.next()
    await state.update_data(numer=int(message.text))
    await message.reply("Rus Tilini Bilish Darajangizni Kiriting", reply_markup=markup2)

@dp.message_handler(state=Form.til)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['til'] = message.text

    await Form.next()
    await message.reply("Qancha Maosh Olishni Xoxlaysiz")

@dp.message_handler(state=Form.oylik)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['oylik'] = message.text

        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Ish Turi: ', data['ish']),
                md.text('F.I.Sh: ', data['ism']),
                md.text("Tug'ulgan Yili: ", data['t_yil']),
                md.text('Yashash Manzili: ', data['manzil']),
                md.text('Telefon Raqami: ', data['numer']),
                md.text('Rus Tilini Bilish Darajasi: ', data['til']),
                md.text('Qancha Maosh Olishni Istashi: ', data['oylik']),
                sep='\n',
            ),
        )
        await bot.send_message(message.chat.id, text="Arizangiz Qabul Qilindi ✅\n\nMalumotlaringiz To'g'ri Kelsa Adminstrator Siz Bilan Bog'lanadi")
        await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
