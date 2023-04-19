from app import celery

from app.note.model import Note

import socketio
import os

from app.note.schema import NoteSchema

# create a Socket.IO client instance
sio = socketio.Client()


@celery.task
def create_note_task(subject, topic, curriculum, level, user_id, audio=None):
    if audio:
        note = Note.create_from_audio(subject, topic, curriculum, level, user_id, audio)
    else:
        note = Note.create(subject, topic, curriculum, level, user_id)

    # connect to the Socket.IO server
    sio.connect(os.environ.get('SOCKET_SERVER'))
    # create a JSON object
    data = NoteSchema().dump(note)

    # emit the JSON data to the server
    sio.emit('json', {'note':data})

    # disconnect from the server
    sio.disconnect()
    return "Note Generated Successfully!"