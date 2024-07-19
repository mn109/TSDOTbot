from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


button_1 = KeyboardButton(text="Наши работы 📺")
button_2 = KeyboardButton(text="Наши соцсети 🔔")
button_3 = KeyboardButton(text="Наши контакты 👋")
button_4 = KeyboardButton(text="Гадание на диагнозах 🔮")


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_1],
        [button_2, button_3],
        [button_4]
        ],
    resize_keyboard=True
    )


psychiatrist_vk_clip_button = InlineKeyboardButton(
    text="Тизер интервью (60 сек.)",
    url="https://vk.com/clip-78784229_456239042"
)

psychiatrist_full_video_button = InlineKeyboardButton(
    text="Видеоинтервью/подкаст (1 ч. 6 мин.)",
    url="https://vk.com/video-78784229_456239048"
)

telegram_channel_button = InlineKeyboardButton(
    text="Канал в Telegram",
    url="https://t.me/mshnktn"
)

vk_public_button = InlineKeyboardButton(
    text="Паблик в VK",
    url="https://vk.com/mshnktn"
)


social_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [telegram_channel_button],
        [vk_public_button]
    ]
)

watch_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [psychiatrist_vk_clip_button],
        [psychiatrist_full_video_button],
    ]
)
