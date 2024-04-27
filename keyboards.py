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


about_us_vk_clip_button = InlineKeyboardButton(
    text="Клип VK (20 сек.)",
    url="https://vk.ru/clip-78784229_456239033"
)

telegram_channel_button = InlineKeyboardButton(
    text="Канал в Telegram",
    url="https://t.me/kamera_k"
)

top_3_button = InlineKeyboardButton(
    text="Ролик для YouTube-канала (107 сек.)",
    url="https://youtu.be/my4feD2Cqgg"
)

top_10_button = InlineKeyboardButton(
    text="Ролик для YouTube-канала (12 мин.)",
    url="https://youtu.be/tUWfljgFJD8"
)

vk_public_button = InlineKeyboardButton(
    text="Паблик в VK",
    url="https://vk.com/kamera_k"
)

website_button = InlineKeyboardButton(
    text="Официальный сайт",
    url="https://kamera-k.ru"
)


social_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [website_button],
        [telegram_channel_button],
        [vk_public_button]
    ]
)

watch_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [top_3_button],
        [top_10_button],
        [about_us_vk_clip_button]
    ]
)
