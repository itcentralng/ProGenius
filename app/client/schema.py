from app import ma
from app.client.model import *

class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client
        exclude = ('is_deleted',)