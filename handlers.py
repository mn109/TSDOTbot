from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards
import random
import time
import data

router = Router()

diagnoses = data.diagnoses
phrases = data.phrases


def get_random_diagnosis() -> str:
    diagnosis = random.choice(data.diagnoses)
    phrase = random.choice(data.phrases)
    final_diagnosis = f"{phrase} {diagnosis[0]}!\n\n{diagnosis[1]}"
    return final_diagnosis


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(data.START_MESSAGE,
                         reply_markup=keyboards.keyboard
                         )


@router.message(F.text == "Наши работы 📺")
@router.message(Command(commands="watch"))
async def process_watch_command(message: Message):
    await message.answer(
        data.WATCH_MESSAGE,
        reply_markup=keyboards.watch_keyboard
        )


@router.message(F.text == "Слушать 🎧")
@router.message(Command(commands="listen"))
async def process_listen_command(message: Message):
    await message.answer(
        data.LISTEN_MESSAGE,
        )

@router.message(F.text == "Наши соцсети 🔔")
@router.message(Command(commands="follow"))
async def process_follow_command(message: Message):
    await message.answer(
        data.FOLLOW_MESSAGE,
        reply_markup=keyboards.social_keyboard
        )

@router.message(F.text == "Наши контакты 👋")
@router.message(Command(commands="connect"))
async def process_connect_command(message: Message):
    await message.answer(
        data.CONNECT_MESSAGE
        )


@router.message(F.text == "Гадание на диагнозах 🔮")
@router.message(Command(commands="divine"))
async def process_divine_command(message: Message):
    time.sleep(1)
    await message.answer("☴")
    time.sleep(1)
    await message.answer(
        get_random_diagnosis()
        )


@router.message()
async def process_other_answers(message: Message):
    await message.answer(
        data.OTHER_MESSAGE
        )
