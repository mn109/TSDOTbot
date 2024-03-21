from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup



button_1 = KeyboardButton(text="Смотреть 📺")
button_2 = KeyboardButton(text="Слушать 🎧")
button_3 = KeyboardButton(text="Подписаться 🔔")
button_4 = KeyboardButton(text="Связаться 👋")
button_5 = KeyboardButton(text="Гадать на диагнозах 🔮")


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_1, button_2],
        [button_3, button_4],
        [button_5]
        ],
    resize_keyboard=True
    )

telegram_channel_button = InlineKeyboardButton(
    text="Канал в Telegram",
    url="https://t.me/xxxxxxxxx"
)

vk_public_button = InlineKeyboardButton(
    text="Паблик в VK",
    url="https://vk.com/xxxxxxxxxx"
)

top_3_button = InlineKeyboardButton(
    text="Топ-3 вопроса стоматологу",
    url="https://youtu.be/my4feD2Cqgg?si=Hch1WC9cR2FfFKRk"
)

social_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [telegram_channel_button],
        [vk_public_button]
    ]
)

watch_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [top_3_button],
    ]
)
