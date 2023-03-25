from datetime import datetime
from app import app, db
from app.user.model import User
from app.call.model import Call

with app.app_context():
    with app.app_context():
        db.create_all()
    print('Ready!')