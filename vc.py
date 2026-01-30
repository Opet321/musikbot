from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types import AudioPiped # Di versi 2.x, ini diimport langsung dari types
from assistant import assistant
# Ubah dari 'queue' menjadi 'helper_queue' sesuai nama file baru kamu
from helper_queue import get_next, has_queue 

pytg = PyTgCalls(assistant)

@pytg.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update):
    chat_id = update.chat_id

    if has_queue(chat_id):
        next_file = get_next(chat_id)
        # Di versi 2.x, gunakan pytg.play bukan change_stream
        await pytg.play(chat_id, AudioPiped(next_file)) 
    else:
        # Di versi 2.x, method ini juga berubah menjadi leave_call
        await pytg.leave_call(chat_id)