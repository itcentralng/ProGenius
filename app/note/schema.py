from app import ma
from app.note.model import *

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        exclude = ('is_deleted',)
    images = ma.Nested('ImageSchema', many=True)