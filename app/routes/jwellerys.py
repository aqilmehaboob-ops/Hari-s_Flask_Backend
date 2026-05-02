from flask import Blueprint, request
from app import db
from ..models import Jwellerys

jwellerys = Blueprint("jwellerys", __name__)

def admin_check(func):
    def inner():
        admin = request.args.get("admin")

        if admin != "hari":
            return {"error": "Forbidden"}, 403
        return func()
    return inner



#Creating jwellery is only allowed by admin
@jwellerys.route("/jwellerys", methods=['POST'])
@admin_check
def create_jwellery():

    data = request.get_json()

    type = data.get('type')
    price = data.get('price')
    code = data.get('code')
    quantity = data.get('quantity')

    if not type or not price or not code\
    or not quantity:
        return {"error": "Invalid data"}, 400
    
    existing_product = Jwellerys.query.filter_by(code=code).first()

    print(existing_product)

    if existing_product:
        existing_product.quantity += quantity
        db.session.commit()
        return{"message": "Product already exists inventory updated"}, 200

    jwellerys = Jwellerys(
        type=type,
        price=price,
        code=code,
        quantity=quantity,
    )

    db.session.add(jwellerys)
    db.session.commit()

    return {"message": "Created"}, 201



@jwellerys.route("/jwellerys", methods=['GET'])
def all_jwellery():

    jwellerys = Jwellerys.query.all()

    print(jwellerys)
    
    lst=[]
    for jwellery in jwellerys:
        lst.append({
            "name": jwellery.type,
            "price": jwellery.price,
            "code": jwellery.code,
            "quantity": jwellery.quantity
        })

    return {"data": lst}, 200

@jwellerys.route("/jwellerys/filter", methods=['GET'])
def filter_jwellerys():
    type = request.args.get("type")

    if not type:
        return {"error": "Invalid data"}, 400

    item = Jwellerys.query.filter_by(type=type).all()

    lst = []

    for i in item:
        lst.append({
            "type": i.type,
            "price": i.price,
            "code": i.code,
            "quantity": i.quantity
        })

    return {"data": lst}, 200
    

