from app import db
from helpers.ai21 import fewShots, improve, noShot

class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String)
    company_description = db.Column(db.String)
    client = db.Column(db.String)
    client_description = db.Column(db.String)
    product = db.Column(db.String)
    product_description = db.Column(db.String)
    components = db.relationship("Component")
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
        return cls.query.filter_by(is_deleted=False).all()
    
    @classmethod
    def create(cls, company, company_description, client, client_description, product, product_description):
        proposal = cls(company=company, company_description=company_description, client=client, client_description=client_description, product=product, product_description=product_description)
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
            content = fewShots(proposal.company, proposal.company_description, proposal.client, proposal.product, proposal.product_description, code)
        else:
            context = "\n\n".join([f"{field.name}\n{field.content}" for field in proposal.components if field.code !='letter'])
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
            if code != 'letter':
                content = fewShots(proposal.company, proposal.company_description, proposal.client, proposal.product, proposal.product_description, code)
            else:
                context = "\n\n".join([f"{field.name}\n{field.content}" for field in proposal.components if field.code !='letter'])
                content = noShot(code, context)
            component.content = content
            component.save()
        else:
            component.regenerate()
        return component