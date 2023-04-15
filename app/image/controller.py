from flask import Blueprint
from app.route_guard import auth_required

from app.image.model import *
from app.image.schema import *

bp = Blueprint('image', __name__)

@bp.post('/image')
@auth_required()
def create_image():
    image = Image.create()
    return ImageSchema().dump(image), 201

@bp.get('/image/<int:id>')
@auth_required()
def get_image(id):
    image = Image.get_by_id(id)
    if image is None:
        return {'message': 'Image not found'}, 404
    return ImageSchema().dump(image), 200

@bp.patch('/image/<int:id>')
@auth_required()
def update_image(id):
    image = Image.get_by_id(id)
    if image is None:
        return {'message': 'Image not found'}, 404
    image.update()
    return ImageSchema().dump(image), 200

@bp.delete('/image/<int:id>')
@auth_required()
def delete_image(id):
    image = Image.get_by_id(id)
    if image is None:
        return {'message': 'Image not found'}, 404
    image.delete()
    return {'message': 'Image deleted successfully'}, 200

@bp.get('/images')
@auth_required()
def get_images():
    images = Image.get_all()
    return ImageSchema(many=True).dump(images), 200