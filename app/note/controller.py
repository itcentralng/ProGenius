from flask import Blueprint, request, g
from app.route_guard import auth_required

from app.note.model import *
from app.note.schema import *

bp = Blueprint('note', __name__)

@bp.post('/note')
@auth_required()
def create_note():
    subject = request.json['subject']
    topic = request.json['topic']
    curriculum = request.json['curriculum']
    level = request.json['level']
    note = Note.create(subject, topic, curriculum, level, g.user.id)
    return NoteSchema().dump(note), 201

@bp.post('/note/audio')
@auth_required()
def create_note_from_audio():
    subject = request.form['subject']
    topic = request.form['topic']
    curriculum = request.form['curriculum']
    level = request.form['level']
    audio = request.files['audio']
    note = Note.create_from_audio(subject, topic, curriculum, level, g.user.id, audio)
    return NoteSchema().dump(note), 201

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
    note = Note.get_by_id(id)
    if note is None:
        return {'message': 'Note not found'}, 404
    note.update()
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