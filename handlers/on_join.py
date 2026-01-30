from pyrogram import filters
from pyrogram.handlers import MessageHandler

async def bot_added(client, message):
    await message.reply(
        "👋 Terima kasih sudah menambahkan bot!\n\n"
        "📌 Jadikan bot ADMIN\n"
        "📌 Tambahkan akun assistant\n"
        "📌 Nyalakan voice chat\n\n"
        "🎵 Gunakan /play"
    )

join_handler = MessageHandler(bot_added, filters.new_chat_members)