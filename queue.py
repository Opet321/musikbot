queues = {}

def add_to_queue(chat_id, file):
    if chat_id not in queues:
        queues[chat_id] = []
    queues[chat_id].append(file)

def get_next(chat_id):
    if chat_id in queues and queues[chat_id]:
        return queues[chat_id].pop(0)
    return None

def has_queue(chat_id):
    return chat_id in queues and len(queues[chat_id]) > 0

def clear_queue(chat_id):
    queues.pop(chat_id, None)