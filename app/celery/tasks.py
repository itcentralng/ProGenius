from app import celery, db
from app.image.schema import ImageSchema

from app.note.model import Note
from app.image.model import Image

import socketio
import os

from app.note.schema import NoteSchema
from helpers.stability import dream
from helpers.upload import add

# create a Socket.IO client instance
sio = socketio.Client()


@celery.task
def create_note_task(subject, topic, curriculum, level, user_id, transient_audio_file=None):
    try:
        if transient_audio_file:
            note = Note.create_from_audio(subject, topic, curriculum, level, user_id, transient_audio_file)
        else:
            note = Note.create(subject, topic, curriculum, level, user_id)
        
        os.remove(transient_audio_file)

        # connect to the Socket.IO server
        sio.connect(os.environ.get('SOCKET_SERVER'))
        # create a JSON object
        data = NoteSchema().dump(note)

        # emit the JSON data to the server
        sio.emit('note', {'note':data})

        # disconnect from the server
        sio.disconnect()
        return "Note Generated Successfully!"
    except Exception as e:
        print(e)
        os.remove(transient_audio_file)
        db.session.rollback()
        return "Note Could Not Be Generated Successfully!"

@celery.task
def regenerate_image(image_id, prompt=None):
    try:
        image = Image.get_by_id(image_id)
        old_prompt = image.prompt
        image.prompt = prompt or image.prompt
        encoded_string = dream(image.prompt)
        image_url = add(encoded_string)
        image.url = image_url
        image.updated_at = db.func.now()

        note = Note.get_by_id(image.note_id)
        note.update_image_prompt(old_prompt, image.prompt)
        
        db.session.commit()
        # connect to the Socket.IO server
        sio.connect(os.environ.get('SOCKET_SERVER'))
        # create a JSON object
        data = ImageSchema().dump(image)

        # emit the JSON data to the server
        sio.emit('image', {'image':data, 'creator_id':note.creator_id})

        # disconnect from the server
        sio.disconnect()
        return "Image Generated Successfully!"
    except Exception as e:
        print(e)
        db.session.rollback()
        return "Image Could Not Be Generated Successfully!"