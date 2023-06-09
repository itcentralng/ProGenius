from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS

# App Config
app = Flask(__name__, )
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)


# Celery
from app.celery import make_celery
celery = make_celery(app)

# Database
from config import secret
app.secret_key = secret
migrate = Migrate(app, db)


# Controllers
from app.user.controller import bp as user_bp
app.register_blueprint(user_bp)
from app.proposal.controller import bp as proposal_bp
app.register_blueprint(proposal_bp)
from app.company.controller import bp as company_bp
app.register_blueprint(company_bp)
from app.client.controller import bp as client_bp
app.register_blueprint(client_bp)

# Error handlers
# from .error_handlers import *