from flask import Blueprint, request, render_template
from app.route_guard import auth_required

from app.call.model import *
from app.call.schema import *

from helpers.openai import chatGPT

bp = Blueprint('call', __name__, template_folder='templates')

@bp.post('/call')
# @auth_required()
def make_response():
    message = request.json.get('message_body')
    Call.create(role='user', content=message)
    history = Call.get_all()
    chat = chatGPT(history)
    Call.create(role='assistant', content=chat.get('content'))
    return chat.get('content')