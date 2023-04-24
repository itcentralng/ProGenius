from flask import Blueprint, request
from app.route_guard import auth_required

from app.client.model import *
from app.client.schema import *

bp = Blueprint('client', __name__)

@bp.post('/client')
@auth_required()
def create_client():
    name = request.json['name']
    address = request.json['address']
    phone = request.json['phone']
    email = request.json['email']
    rep = request.json['rep']
    role = request.json['role']
    description = request.json['description']
    client = Client.create(name, address, phone, email, rep, role, description)
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
    name = request.json.get('name')
    address = request.json.get('address')
    phone = request.json.get('phone')
    email = request.json.get('email')
    rep = request.json.get('rep')
    role = request.json.get('role')
    description = request.json.get('description')
    client.update(name, address, phone, email, rep, role, description)
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