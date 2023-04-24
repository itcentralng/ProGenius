from app import db
from flask import g

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    rep = db.Column(db.String)
    role = db.Column(db.String)
    description = db.Column(db.String)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, name=None, address=None, phone=None, email=None, rep=None, role=None, description=None):
        self.name = name or self.name
        self.address = address or self.address
        self.phone = phone or self.phone
        self.email = email or self.email
        self.rep = rep or self.rep
        self.role = role or self.role
        self.description = description or self.description
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
    def get_all(cls):
        return cls.query.filter_by(is_deleted=False, created_by=g.user.id).all()
    
    @classmethod
    def create(cls, name=None, address=None, phone=None, email=None, rep=None, role=None, description=None):
        company = cls(name=name, address=address, phone=phone, email=email, rep=rep, role=role, description=description, created_by=g.user.id)
        company.save()
        return company