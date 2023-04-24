from flask import Blueprint
from app.route_guard import auth_required

from app.company.model import *
from app.company.schema import *

bp = Blueprint('company', __name__)

@bp.post('/company')
@auth_required()
def create_company():
    company = Company.create()
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
    company.update()
    return CompanySchema().dump(company), 200

@bp.delete('/company/<int:id>')
@auth_required()
def delete_company(id):
    company = Company.get_by_id(id)
    if company is None:
        return {'message': 'Company not found'}, 404
    company.delete()
    return {'message': 'Company deleted successfully'}, 200

@bp.get('/companys')
@auth_required()
def get_companys():
    companys = Company.get_all()
    return CompanySchema(many=True).dump(companys), 200