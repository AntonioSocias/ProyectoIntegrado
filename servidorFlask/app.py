# app.py
from flask import Flask
from flask_cors import CORS
from models import db, ma
from routes import register_crud_endpoints
from custom_routes import register_custom_endpoints
import config

app = Flask(__name__)
app.secret_key = 'clave-super-secreta'

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
ma.init_app(app)
CORS(app)

with app.app_context():
    register_crud_endpoints(app)
    register_custom_endpoints(app)

if __name__ == '__main__':
    app.run(debug=True)
