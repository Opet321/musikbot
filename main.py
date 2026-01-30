from pyrogram import Client
from config import BOT_TOKEN
from assistant import assistant
from vc import pytg
from handlers.start import start_handler
from handlers.play import play_handler
from handlers.video import video_handler
from handlers.admin import admin_handler
from handlers.on_join import join_handler

bot = Client("bot", bot_token=BOT_TOKEN)

bot.add_handler(start_handler)
bot.add_handler(play_handler)
bot.add_handler(video_handler)
bot.add_handler(admin_handler)
bot.add_handler(join_handler)

assistant.start()
pytg.start()
bot.run()