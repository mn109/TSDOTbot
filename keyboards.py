from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


button_1 = KeyboardButton(text="Наши работы 📺")
button_2 = KeyboardButton(text="Слушать 🎧")
button_3 = KeyboardButton(text="Наши соцсети 🔔")
button_4 = KeyboardButton(text="Наши контакты 👋")
button_5 = KeyboardButton(text="Гадание на диагнозах 🔮")


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_1],
        [button_3, button_4],
        [button_5]
        ],
    resize_keyboard=True
    )


about_us_vk_clip_button = InlineKeyboardButton(
    text="Клип VK (20 сек.)",
    url="https://vk.ru/clip-78784229_456239033"
)

neuroscience_promo_button = InlineKeyboardButton(
    text="Информационный ролик (5 мин.)",
    url="https://vk.com/video-78784229_456239040"
)

orthodontist_vk_clip_button = InlineKeyboardButton(
    text="Клип VK (52 сек.)",
    url="https://vk.com/clip-78784229_456239039"
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
        [telegram_channel_button],
        [vk_public_button]
    ]
)

watch_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [psychiatrist_vk_clip_button],
        [psychiatrist_full_video_button],
        [orthodontist_vk_clip_button],
        [about_us_vk_clip_button],
        [neuroscience_promo_button],
        [top_3_button],
        [top_10_button]
    ]
)
