from flask import Blueprint, request, g
from app.route_guard import auth_required

from app.note.model import *
from app.note.schema import *

from app.celery.tasks import create_note_task
from helpers.ephemeral import Ephemeral

bp = Blueprint('note', __name__)

@bp.post('/note')
@auth_required()
def create_note():
    subject = request.json['subject']
    topic = request.json['topic']
    curriculum = request.json['curriculum']
    level = request.json['level']
    create_note_task.delay(subject, topic, curriculum, level, g.user.id)
    return {'status':'success', 'message':'Note is being generated, please hold'}, 200

@bp.post('/note/audio')
@auth_required()
def create_note_from_audio():
    subject = request.form['subject']
    topic = request.form['topic']
    curriculum = request.form['curriculum']
    level = request.form['level']
    audio = request.files['audio']
    transient_audio_file = Ephemeral(audio)
    create_note_task.delay(subject, topic, curriculum, level, g.user.id, transient_audio_file.save())
    return {'status':'success', 'message':'Note is being generated, please hold'}, 200

@bp.get('/note/<int:id>')
@auth_required()
def get_note(id):
    note = Note.get_by_id(id)
    if note is None:
        return {'message': 'Note not found'}, 404
    return NoteSchema().dump(note), 200

@bp.patch('/note/<int:id>')
@auth_required()
def update_note(id):
    clean = request.json.get('content', 'clean')
    raw = request.json.get('raw')
    subject = request.json.get('subject')
    topic = request.json.get('topic')
    level = request.json.get('level')
    curriculum = request.json.get('curriculum')
    note = Note.get_by_id(id)
    if note is None:
        return {'message': 'Note not found'}, 404
    note.update(subject, topic, level, curriculum, raw, clean)
    return NoteSchema().dump(note), 200

@bp.delete('/note/<int:id>')
@auth_required()
def delete_note(id):
    note = Note.get_by_id(id)
    if note is None:
        return {'message': 'Note not found'}, 404
    note.delete()
    return {'message': 'Note deleted successfully'}, 200

@bp.get('/notes')
@auth_required()
def get_notes():
    notes = Note.get_all_by_creator_id(g.user.id)
    return NoteSchema(many=True).dump(notes), 200