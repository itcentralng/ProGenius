from app import ma
from app.proposal.model import *

class ProposalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Proposal
        exclude = ('is_deleted',)