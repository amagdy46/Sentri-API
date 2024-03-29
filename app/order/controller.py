from flask import jsonify, request
from flask_restx import Resource, Namespace, reqparse
# from flask_jwt_extended import (
#     jwt_required, create_access_token,
#     get_jwt_identity
# )
import app.resources.helper_functions as helper
from ..catalog.model import Catalog
from .model import Order
from .schema import OrderSchema
from app.customer.model import Customer
from app.vendor.model import Vendor
from app.models.bot import Bot
from app.models.button import ButtonTemplate
api = Namespace('Order')


@api.route('/<string:order_number>')
class OrderResourceByNumber(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('order_status')
    parser.add_argument('order_number')

    def get(self):
        pass

    def post(self):
        pass

    def put(self, order_number):
        data = request.get_json()
        print(data)
        print(order_number)
        order = Order.find_by_number(order_number)
        if order:
            try:
                order.update({'status': request.form.get('order_status')})
                order.save()
                return 'Order Status was edited', 200
            except Exception as e:
                raise e
        return 'Order Not Found', 404

    def delete(self, order_number):
        order = Order.find_by_number(order_number)
        if order:
            try:
                order.delete()
                return 'Oder was Deleted', 200
            except Exception as e:
                raise e
        return 'Order Not Found', 404


@api.route('/psid/<string:psid>')
class OrderResourceByPsid(Resource):
    def get(self, psid):
        order = Order.query.filter_by(psid=psid, is_confirmed=False).first()
        if order:
            print(order)
            output = OrderSchema().dump(order)
            return jsonify(output)
        else:
            return 'Customer not found', 404

    def put(self, psid):
        customer = Customer.find_by_psid(psid)
        order = Order.query.filter_by(psid=psid, is_confirmed=False).first()
        vendor = Vendor.find_by_page_id(customer.page_id)
        catalog = Catalog.find_by_page_id(vendor.page_id)
        knowledge = catalog.knowledge
        bot = Bot(access_token=vendor.page_access_token)
        data = request.get_json()
        print(data)
        if not data['items']:
            bot.send_text_message(psid, 'انت لم تطلب شيء بعد!')
            return 'Order is empty', 200
        order.item = data['items']
        order.save()
        confirm_block = ButtonTemplate()
        confirm_block.add_web_url(
            **{knowledge['buttons']['values']['Confirm_Order']: 'https://rest-bot-dev.herokuapp.com/confirm_order'})
        confirm_block.add_postback(
            **{knowledge['buttons']['values']['Add_to_Order']: 'main_menu'})
        confirm_block.add_web_url(
            **{knowledge['buttons']['values']['Edit_Order']: 'https://rest-bot-dev.herokuapp.com/edit_order'})

        confirm_block.set_text('تم تعديل الأوردر الخاص بك')
        bot.send_template_message(
            psid, {'payload': confirm_block.get_template()})
        return'Order was Edited', 200


@api.route('/item/<string:sender_id>/<string:item_id>/')
class OrderItem(Resource):
    def get(self):
        pass

    def post(self, sender_id, item_id):
        customer = Customer.find_by_psid(sender_id)
        vendor = customer.vendor
        catalog = Catalog.find_by_page_id(vendor.page_id)
        item = catalog.items[item_id]
        knowledge = catalog.knowledge
        bot = Bot(access_token=vendor.page_access_token)
        order = helper.get_order_from_customer(customer)
        print(order)
        # if not vendor.is_open():
        #     bot.send_text_message(sender_id,
        #                           knowledge['browse']['values']['Business_Closed_Message'])
        #     return 'Vendor is Closed', 200
        if order is None or order.is_confirmed:
            order = Order(sender_id, vendor.page_id)
        order_item = {}
        order_item['quantity'] = request.form.get('quantity')
        if request.form.get('notes') is not None:
            order_item['notes'] = request.form.get('notes')
        order_item['category'] = item['category_title']
        order_item['name'] = item['title']
        order_item['price'] = item['price']
        order.add_item(order_item)
        confirm_block = ButtonTemplate()
        confirm_block.add_web_url(
            **{knowledge['buttons']['values']['Confirm_Order']: 'https://rest-bot-dev.herokuapp.com/confirm_order'})
        confirm_block.add_postback(
            **{knowledge['buttons']['values']['Add_to_Order']: 'main_menu'})
        confirm_block.add_web_url(
            **{knowledge['buttons']['values']['Edit_Order']: 'https://rest-bot-dev.herokuapp.com/edit_order'})

        text = '{} * {} تمت اضافته للأوردو الخاص بك'.format(order_item['quantity'],
                                                            order_item['name'])
        confirm_block.set_text(text)
        bot.send_template_message(
            sender_id, {'payload': confirm_block.get_template()})
        return 'Item added to Order', 200

        def put(self, sender_id):
            pass
