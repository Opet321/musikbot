from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME, BOT_USERNAME

async def start(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Tambahkan Bot ke Grup",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                )
            ]
        ]
    )

    await message.reply(
        f"🎵 **{BOT_NAME}**\n\n"
        "Bot Music & Video Voice Chat\n\n"
        "1️⃣ Tambahkan bot ke grup\n"
        "2️⃣ Jadikan admin\n"
        "3️⃣ Nyalakan voice chat\n\n"
        "Gunakan /play untuk mulai.",
        reply_markup=keyboard
    )

start_handler = MessageHandler(start, filters.command("start"))