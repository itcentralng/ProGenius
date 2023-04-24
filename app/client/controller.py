from flask import Blueprint
from app.route_guard import auth_required

from app.client.model import *
from app.client.schema import *

bp = Blueprint('client', __name__)

@bp.post('/client')
@auth_required()
def create_client():
    client = Client.create()
    return ClientSchema().dump(client), 201

@bp.get('/client/<int:id>')
@auth_required()
def get_client(id):
    client = Client.get_by_id(id)
    if client is None:
        return {'message': 'Client not found'}, 404
    return ClientSchema().dump(client), 200

@bp.patch('/client/<int:id>')
@auth_required()
def update_client(id):
    client = Client.get_by_id(id)
    if client is None:
        return {'message': 'Client not found'}, 404
    client.update()
    return ClientSchema().dump(client), 200

@bp.delete('/client/<int:id>')
@auth_required()
def delete_client(id):
    client = Client.get_by_id(id)
    if client is None:
        return {'message': 'Client not found'}, 404
    client.delete()
    return {'message': 'Client deleted successfully'}, 200

@bp.get('/clients')
@auth_required()
def get_clients():
    clients = Client.get_all()
    return ClientSchema(many=True).dump(clients), 200