from flask import Blueprint, request
from ..models import Cart, Jwellerys
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

cart = Blueprint("cart", __name__)

@cart.route("/cart", methods=['POST'])
@jwt_required()
def add_to_cart():

    data = request.get_json()

    if not data:
        return {"error": "Invalid data"}, 400
    
    identity = get_jwt_identity()

    jwellery_id = data.get('jwellery_id')
    quantity = data.get('quantity')

    if not jwellery_id or not quantity:
        return {"error": "Invalid data"}, 400
    
    
    
    cart = Cart(jwellery_id=jwellery_id, user_id=identity, quantity=quantity)

    db.session.add(cart)
    db.session.commit()
    
    return {"message": "added to cart"}, 200



@cart.route("/cart", methods=['GET'])
@jwt_required()
def view_cart():

    identity = get_jwt_identity()

    items = Cart.query.filter_by(user_id=identity).all()

    lst = []
    for item in items:
        jwellery = Jwellerys.query.filter_by(id=item.jwellerys_id).first_or_404()

        lst.append({
            "type": jwellery.type,
            "code": jwellery.code,
            "price": jwellery.price,
            "quantity": item.quantity

        })

    return {"data": lst}, 200





@cart.route("/cart/<int:jwellery_id>", methods=['DELETE'])
@jwt_required()
def remove_from_cart(jwellery_id):

    identity = get_jwt_identity()

    item = Cart.query.filter_by(jwellery_id=jwellery_id, user_id=identity).first_or_404()

    db.session.delete(item)
    db.session.commit()

    return {"message": "Item removed from cart"}, 200