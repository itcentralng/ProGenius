from flask import Blueprint, request
from app.route_guard import auth_required

from app.company.model import *
from app.company.schema import *

bp = Blueprint('company', __name__)

@bp.post('/company')
@auth_required()
def create_company():
    name = request.json['name']
    address = request.json['address']
    phone = request.json['phone']
    rep = request.json['rep']
    description = request.json['description']
    company = Company.create(name, address, phone, rep, description)
    return CompanySchema().dump(company), 201

@bp.get('/company/<int:id>')
@auth_required()
def get_company(id):
    company = Company.get_by_id(id)
    if company is None:
        return {'message': 'Company not found'}, 404
    return CompanySchema().dump(company), 200

@bp.patch('/company/<int:id>')
@auth_required()
def update_company(id):
    company = Company.get_by_id(id)
    if company is None:
        return {'message': 'Company not found'}, 404
    name = request.json.get('name')
    address = request.json.get('address')
    phone = request.json.get('phone')
    rep = request.json.get('rep')
    description = request.json.get('description')
    company.update(name, address, phone, rep, description)
    return CompanySchema().dump(company), 200

@bp.delete('/company/<int:id>')
@auth_required()
def delete_company(id):
    company = Company.get_by_id(id)
    if company is None:
        return {'message': 'Company not found'}, 404
    company.delete()
    return {'message': 'Company deleted successfully'}, 200

@bp.get('/companies')
@auth_required()
def get_companies():
    companys = Company.get_all()
    return CompanySchema(many=True).dump(companys), 200