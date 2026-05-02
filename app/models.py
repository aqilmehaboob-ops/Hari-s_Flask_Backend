from app import db
import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))

class Jwellerys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))
    price = db.Column(db.Integer)
    code = db.Column(db.String, unique=True)
    quantity = db.Column(db.Integer)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jwellery_id = db.Column(db.Integer, db.ForeignKey('jwellerys.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    quantity = db.Column(db.Integer)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    total_price = db.Column(db.Integer)
    status = db.Column(db.String, default="pending")
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Order_Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    jwellerys_id = db.Column(db.Integer, db.ForeignKey('jwellerys.id'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)


