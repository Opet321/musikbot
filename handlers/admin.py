from pyrogram import filters
from pyrogram.handlers import MessageHandler
from vc import pytg
from queue import get_next, clear_queue
from pytgcalls.types.input_stream import AudioPiped

async def skip(client, message):
    chat_id = message.chat.id
    next_song = get_next(chat_id)
    if not next_song:
        await message.reply("❌ Antrian kosong")
        return

    await pytg.change_stream(chat_id, AudioPiped(next_song))
    await message.reply("⏭ Lagu berikutnya")

async def stop(client, message):
    chat_id = message.chat.id
    clear_queue(chat_id)
    await pytg.leave_group_call(chat_id)
    await message.reply("⏹ Keluar voice chat")

admin_handler = MessageHandler(skip, filters.command("skip"))