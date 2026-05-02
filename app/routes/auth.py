from flask import Blueprint, request
from ..models import Users
from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=['POST'])
def register():

    data = request.get_json()

    name = data.get('name')
    password = data.get('password')
    email = data.get('email')

    if not name or not password or not email:
        return {"error": "Inavlid data"}, 400
    
    hashed_password = generate_password_hash(password)
    
    existing_email = Users.query.filter_by(email=email).first()

    if existing_email:
        return {"message": "Email already exists"}, 400

    users = Users(name=name, password=hashed_password, email=email)

    db.session.add(users)
    db.session.commit()

    return {"message": "User created"}, 201



@auth.route("/login", methods=['POST'])
def login():

    data = request.get_json()

    name = data.get('name')
    password = data.get('password')

    if not name or not password:
        return {"error": "Inavlid data"}, 400
    
    user = Users.query.filter_by(name=name).first_or_404()

    if not check_password_hash(user.password, password):
        return {"error": "Incorrect password"}, 400

    acess_token = create_access_token(identity=str(user.id))

    return {
        "message": "login successful",
        "access_token": acess_token
        }, 200

    



