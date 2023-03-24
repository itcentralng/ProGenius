from flask import Blueprint, request, render_template
from app.route_guard import auth_required

# from app.call.model import *
# from app.call.schema import *

bp = Blueprint('call', __name__, template_folder='templates')

@bp.post('/call')
# @auth_required()
def make_response():
    r = request.json.get('message_body')
    return "You said: " + r + "." + " I'm sorry, I don't understand.", 200