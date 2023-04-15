from app import db
from helpers.openai import chat
from helpers.formater import clean

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subject = db.Column(db.String)
    topic = db.Column(db.String)
    level = db.Column(db.String)
    curriculum = db.Column(db.String)
    raw = db.Column(db.String)
    clean = db.Column(db.String)
    images = db.relationship('Image')
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, subject=None, topic=None, level=None, curriculum=None, raw=None, clean=None):
        self.subject = subject or self.subject
        self.topic = topic or self.topic
        self.level = level or self.level
        self.curriculum = curriculum or self.curriculum
        self.raw = raw or self.raw
        self.clean = clean or self.clean
        self.updated_at = db.func.now()
        db.session.commit()
    
    def delete(self):
        self.is_deleted = True
        self.updated_at = db.func.now()
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id, is_deleted=False).first()
    
    @classmethod
    def get_all_by_creator_id(cls, creator_id):
        return cls.query.filter_by(is_deleted=False, creator_id=creator_id).all()
    
    @classmethod
    def create(cls, subject, topic, curriculum, level):
        note = cls(subject=subject, topic=topic, curriculum=curriculum, level=level)
        note.save()
        raw = chat(subject, topic, curriculum, level)
        # print(response)
        note.update(raw=raw, clean=clean(raw, note.id))
        # print(formatted)
        return note
        # return Note()