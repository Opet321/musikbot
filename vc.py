from pytgcalls import PyTgCalls
from pytgcalls import types
from pytgcalls.types import media 
from assistant import assistant
from helper_queue import get_next, has_queue 

pytg = PyTgCalls(assistant)

@pytg.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: types.Update):
    chat_id = update.chat_id

    if has_queue(chat_id):
        next_file = get_next(chat_id)
        await pytg.play(chat_id, media.AudioPiped(next_file))
    else:
        await pytg.leave_call(chat_id)