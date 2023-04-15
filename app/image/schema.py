from app import ma
from app.image.model import *

class ImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Image
        exclude = ('is_deleted',)