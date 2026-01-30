from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types import AudioPiped # Hapus '.input_stream'
from assistant import assistant
from queue import get_next, has_queue

pytg = PyTgCalls(assistant)

@pytg.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update):
    chat_id = update.chat_id

    if has_queue(chat_id):
        next_file = get_next(chat_id)
        await pytg.play(chat_id, AudioPiped(next_file))
    else:
        await pytg.leave_group_call(chat_id)