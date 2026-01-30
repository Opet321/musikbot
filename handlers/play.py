from pyrogram import filters
from pyrogram.handlers import MessageHandler
from downloader import download
from queue import add_to_queue, get_next
from vc import pytg
from pytgcalls.types.input_stream import AudioPiped

async def play(client, message):
    chat_id = message.chat.id
    query = " ".join(message.command[1:])

    if not query:
        await message.reply("❌ Masukkan judul lagu")
        return

    file = download(query)
    add_to_queue(chat_id, file)

    if chat_id not in pytg.active_calls:
        await pytg.join_group_call(
            chat_id,
            AudioPiped(get_next(chat_id))
        )
        await message.reply("🎵 Memutar lagu")
    else:
        await message.reply("➕ Ditambahkan ke antrian")

play_handler = MessageHandler(play, filters.command("play"))