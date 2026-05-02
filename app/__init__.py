from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///hari.db"
    app.config['JWT_SECRET_KEY'] = "super-secret"

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.users import users
    from app.routes.auth import auth
    from app.routes.jwellerys import jwellerys
    from app.routes.orders import orders
    from app.routes.cart import cart


    app.register_blueprint(cart)
    app.register_blueprint(users)
    app.register_blueprint(auth)
    app.register_blueprint(jwellerys)
    app.register_blueprint(orders)

    return app
