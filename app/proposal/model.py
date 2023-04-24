from app import db
from helpers.ai21 import fewShots, improve, noShot
from flask import g
from app.company.model import Company
from app.client.model import Client

class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"))
    offering = db.Column(db.String)
    description = db.Column(db.String)
    components = db.relationship("Component")
    company = db.relationship("Company")
    client = db.relationship("Client")
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.updated_at = db.func.now()
        db.session.commit()
    
    def delete(self):
        self.is_deleted = True
        self.updated_at = db.func.now()
        db.session.commit()
    
    def create_field(self, component, index):
        Component.create(self.id, index, component)
        self.update()
    
    def improve_field(self, component):
        component = Component.get_by_proposal_id_and_code(self.id, component)
        component.improve_content()
        self.update()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id, is_deleted=False).first()
    
    @classmethod
    def get_all(cls):
        return cls.query.filter_by(is_deleted=False, created_by=g.user.id).all()
    
    @classmethod
    def create(cls, company_id, client_id, offering, description):
        proposal = cls(company_id=company_id, client_id=client_id, offering=offering, description=description, created_by=g.user.id)
        proposal.save()
        return proposal

class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey("proposal.id"))
    index = db.Column(db.Integer)
    code = db.Column(db.String)
    name = db.Column(db.String)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, index=None, code=None, name=None, content=None):
        self.index = index or self.index
        self.code = code or self.code
        self.name = name or self.name
        self.content = content or self.content
        self.updated_at = db.func.now()
        db.session.commit()
    
    def improve_content(self):
        content = improve(self.content)
        self.update(content=content)
    
    def regenerate(self):
        proposal = Proposal.get_by_id(self.proposal_id)
        if self.code != 'letter':
            content = fewShots(proposal.company.name, proposal.company.description, proposal.client.name, proposal.offering, proposal.description, self.code)
        else:
            context = "\n\n".join([f"{field.name}\n{field.content}" for field in proposal.components if field.code !='letter'])
            context+= f"""
            \n
            Sender:
                Name: {proposal.company.rep},
                Address: {proposal.company.address},
                Phone: {proposal.company.phone},
            Receiver:
                Name: {proposal.client.rep},
                Address: {proposal.client.address},
                Phone: {proposal.client.phone},
            """
            content = noShot(self.code, context)
        self.update(content=content)
    
    def delete(self):
        self.is_deleted = True
        self.updated_at = db.func.now()
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id, is_deleted=False).first()
    
    @classmethod
    def get_by_proposal_id_and_code(cls, proposal_id, code):
        return cls.query.filter_by(proposal_id=proposal_id, code=code, is_deleted=False).first()
    
    @classmethod
    def get_all(cls):
        return cls.query.filter_by(is_deleted=False).all()
    
    @classmethod
    def create(cls, proposal_id, index, code):
        proposal = Proposal.get_by_id(proposal_id)
        component = cls.get_by_proposal_id_and_code(proposal.id, code)
        if not component:
            component = cls(proposal_id=proposal.id, index=index, code=code, name=code.title())
            component.save()
        component.regenerate()
        return component