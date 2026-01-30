from pyrogram import filters
from pyrogram.handlers import MessageHandler
from downloader import download
from queue import add_to_queue
from vc import pytg
from pytgcalls.types.input_stream import AudioVideoPiped

async def vplay(client, message):
    chat_id = message.chat.id
    query = " ".join(message.command[1:])

    file = download(query)
    add_to_queue(chat_id, file)

    if chat_id not in pytg.active_calls:
        await pytg.join_group_call(
            chat_id,
            AudioVideoPiped(file)
        )
        await message.reply("🎬 Memutar video")
    else:
        await message.reply("➕ Video masuk antrian")

video_handler = MessageHandler(vplay, filters.command("vplay"))