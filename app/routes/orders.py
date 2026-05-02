from flask import Blueprint, request
from ..models import Orders, Jwellerys, Order_Items
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

orders = Blueprint("orders", __name__)

@orders.route("/orders", methods=['POST'])
@jwt_required()
def place_order():

    data = request.get_json()

    identity = get_jwt_identity()
    jwellery_id = data.get('jwellery_id')
    quantity = data.get('quantity')

    if not jwellery_id or not quantity:
        return {"error": "Invalid data"}, 400
    
    jwellerys = Jwellerys.query.filter_by(id=int(jwellery_id)).first_or_404()
    price = jwellerys.price
    total_price = quantity * price

    if jwellerys.quantity <= 0:
        return {"error": "Out of stock"}, 400
    jwellerys.quantity -= quantity
    db.session.commit()

    orders = Orders(user_id=identity, total_price=total_price)
    db.session.add(orders)
    db.session.commit()

    order_item = Order_Items(order_id=orders.id, jwellerys_id=jwellerys.id, quantity=quantity, price=price)
    db.session.add(order_item)
    db.session.commit()

    return "order placed", 200