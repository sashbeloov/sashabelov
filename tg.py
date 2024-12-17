
from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
import asyncio
from database_zayavka import save_info 



TOKEN = "7732796276:AAHeZnX3s3hM5vcid9_vvPIuwLw6sLaz-Kg"

ChannelName = "@zayavkalar_infosi"

bot = Bot(token=TOKEN)

dp = Dispatcher()

user_data = {}

@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == "/start" or message.text == "Zayavka qoldirish":
        await start(message)
    elif "name" not in user_data[user_id]:
        await ask_phone(message)
    elif 'phone' not in user_data[user_id]:
        await ask_age(message)
    elif 'age' not in user_data[user_id]:
        await total_info(message)


@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    await message.answer("Assalomu aleykum! \nIltimos ismingiz kiriting:")
    print(user_data)




async  def ask_phone(message: types.Message):            
    user_id = message.from_user.id                          
    name = message.text                                  
    user_data[user_id]["name"] = name                  
    button = [
        [types.KeyboardButton(text="Raqam jo'natish", request_contact=True)]       
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)     
    await  message.answer("Iltimos telefon raqamingizni kiriting", reply_markup=keyboard)      
    print(user_data)                


async def ask_age(message: types.Message):
    user_id = message.from_user.id
    if message.contact is not None:
        phone = message.contact.phone_number

    else:
        phone = message.text
    user_data[user_id]['phone'] = phone
    await message.answer("Iltimos yoshingizni kiriting: ")
    print(user_data)

