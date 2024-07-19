from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards
import random
import time
import json

router = Router()

with open('messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

with open('phrases.json', 'r', encoding='utf-8') as f:
    phrases_data = json.load(f)

with open('diagnoses.json', 'r', encoding='utf-8') as f:
    diagnoses_data = json.load(f)

START_MESSAGE = messages["START_MESSAGE"]
WATCH_MESSAGE = messages["WATCH_MESSAGE"]
FOLLOW_MESSAGE = messages["FOLLOW_MESSAGE"]
CONNECT_MESSAGE = messages["CONNECT_MESSAGE"]
OTHER_MESSAGE = messages["OTHER_MESSAGE"]

phrases = phrases_data["phrases"]
diagnoses = diagnoses_data["diagnoses"]

last_divination = None

def get_random_diagnosis() -> str:
    global last_divination
    while True:
        diagnosis = random.choice(diagnoses)
        final_diagnosis = f"{diagnosis[0]}!\n\n{diagnosis[1]}"
        if final_diagnosis != last_divination:
            last_divination = final_diagnosis
            return final_diagnosis

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(START_MESSAGE, reply_markup=keyboards.keyboard)

@router.message(F.text == "Наши работы 📺")
@router.message(Command(commands="watch"))
async def process_watch_command(message: Message):
    await message.answer(WATCH_MESSAGE, reply_markup=keyboards.watch_keyboard)

@router.message(F.text == "Наши соцсети 🔔")
@router.message(Command(commands="follow"))
async def process_follow_command(message: Message):
    await message.answer(FOLLOW_MESSAGE, reply_markup=keyboards.social_keyboard)

@router.message(F.text == "Наши контакты 👋")
@router.message(Command(commands="connect"))
async def process_connect_command(message: Message):
    await message.answer(CONNECT_MESSAGE)

@router.message(F.text == "Гадание на диагнозах 🔮")
@router.message(Command(commands="divine"))
async def process_divine_command(message: Message):
    time.sleep(1)
    await message.answer("☴")
    time.sleep(1)
    await message.answer(get_random_diagnosis())

@router.message()
async def process_other_answers(message: Message):
    await message.answer(OTHER_MESSAGE)
