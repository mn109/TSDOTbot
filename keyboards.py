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

youtube_button = InlineKeyboardButton(
    text="YouTube-канал",
    url="https://youtu.be/DD8CDHDSwl0?si=MBut-J_3hYnDe0ym"
)

social_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [telegram_channel_button],
        [vk_public_button]
    ]
)

watch_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [youtube_button],
    ]
)
