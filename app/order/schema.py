from app import ma
from .model import Order
# from app.vendor.schema import VendorSchema
from app.customer.schema import CustomerSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
    customer = ma.Nested(CustomerSchema)
    # vendor = ma.Nested(VendorSchema)
