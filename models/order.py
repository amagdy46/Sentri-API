from db import db, ma
import datetime
from sqlalchemy_json import NestedMutableJson
import random


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    items = db.Column(NestedMutableJson)
    total = db.Column(db.Float(precision=3))
    is_confirmed = db.Column(db.Boolean, default=False)
    time = db.Column(db.DateTime)
    psid = db.Column(db.String, db.ForeignKey('users.psid'))

    def __init__(self, psid):
        self.psid = psid
        self.time = datetime.datetime.utcnow()
        self.number = random.randint(1000, 99999)
        self.items = []
        self.total = 0
        self.is_confirmed = False

    @classmethod
    def find_by_number(cls, number):
        return cls.query.filter_by(number=number).first()

    @classmethod
    def find_by_user_id(cls, psid):
        return cls.query.filter_by(user_id=psid).first()

    def add_item(self, name, quantity, _type, notes, price, combo):
        item = {}
        item['name'] = name
        item['quantity'] = float(quantity)
        item['type'] = _type
        item['notes'] = notes
        item['combo'] = float(combo)

        item['price'] = float(price)
        # j_item = json.dumps(item)
        self.items.append(item)
        item_price = float(price) + float(combo)
        self.total += item_price * float(quantity)
        self.save()

    def edit(self):
        pass

    def save(self):
        db.session.add(self)
        db.session.commit()

    def cancel(self):
        db.session.delete(self)
        db.session.commit()

    def confirm(self):
        self.is_confirmed = True
        self.save()


class OrderSchema(ma.ModelSchema):
    class Meta:
        model = Order
