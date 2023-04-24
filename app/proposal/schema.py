from app import ma
from app.proposal.model import *


class ComponentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Component
        exclude = ('is_deleted',)
class ProposalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Proposal
        exclude = ('is_deleted',)
    components = ma.Nested('ComponentSchema', many=True)