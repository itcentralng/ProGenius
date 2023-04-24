from flask import Blueprint, request
from app.route_guard import auth_required

from app.proposal.model import *
from app.proposal.schema import *

bp = Blueprint('proposal', __name__)

@bp.post('/proposal')
@auth_required()
def create_proposal():
    company_id = request.json['company_id']
    client_id = request.json['client_id']
    offering = request.json['offering']
    description = request.json['description']
    proposal = Proposal.create(company_id, client_id, offering, description)
    return ProposalSchema().dump(proposal), 201

@bp.post('/proposal/<int:id>')
@auth_required()
def create_field(id):
    component = request.json['component']
    index = request.json['index']
    proposal = Proposal.get_by_id(id)
    proposal.create_field(component, index)
    return ProposalSchema().dump(proposal), 201

@bp.post('/proposal/improve/<int:id>')
@auth_required()
def improve_field(id):
    component = request.json['component']
    proposal = Proposal.get_by_id(id)
    proposal.improve_field(component)
    return ProposalSchema().dump(proposal), 201

@bp.get('/proposal/<int:id>')
@auth_required()
def get_proposal(id):
    proposal = Proposal.get_by_id(id)
    if proposal is None:
        return {'message': 'Proposal not found'}, 404
    return ProposalSchema().dump(proposal), 200

@bp.patch('/proposal/<int:id>')
@auth_required()
def update_proposal(id):
    proposal = Proposal.get_by_id(id)
    if proposal is None:
        return {'message': 'Proposal not found'}, 404
    proposal.update()
    return ProposalSchema().dump(proposal), 200

@bp.delete('/proposal/<int:id>')
@auth_required()
def delete_proposal(id):
    proposal = Proposal.get_by_id(id)
    if proposal is None:
        return {'message': 'Proposal not found'}, 404
    proposal.delete()
    return {'message': 'Proposal deleted successfully'}, 200

@bp.get('/proposals')
@auth_required()
def get_proposals():
    proposals = Proposal.get_all()
    return ProposalSchema(many=True).dump(proposals), 200