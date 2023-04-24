from app import ma
from app.company.model import *

class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        exclude = ('is_deleted',)