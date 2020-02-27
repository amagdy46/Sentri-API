from flask import Blueprint, render_template, request
import json
from datetime import datetime
import ast
from models.bot import Bot
import resources.helper_functions as helper
# Set up a Blueprint
webhook_bp = Blueprint('webhook_bp', __name__,
                       template_folder='templates',
                       static_folder='static')

VERIFICATION_TOKEN = 'test'


@webhook_bp.route('/webhook', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFICATION_TOKEN:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200


@webhook_bp.route('/webhook', methods=['POST'])
def handle_incoming_messages():
    data = request.get_json()
    print(data)
    webhook_type = helper.get_type_from_payload(data)
    page_id = helper.get_vendor_from_message(data)
    vendor = helper.handle_vendor(page_id)
    bot = Bot(access_token=vendor.access_token)
    sender_id = helper.get_customer_from_message(data)
    customer = helper.handle_customer(sender_id, page_id)
    print(sender_id)
    print(webhook_type)
    bot.send_before_message(sender_id)
    # if not vendor.is_open():
    #     bot.send_text_message(
    #         sender_id, 'المطعم مغلق حاليا \nالرجاء المحاولة مرة أخرى خلال مواعيد العمل الرسمية من {} الى {}'.format(vendor.opening_hours.strftime('%H:%M'), vendor.closing_hours.strftime('%H:%M')))
    #     return 'Vendor is Closed', 200
    if webhook_type == "text":
        # HANDLE TEXT MESSAGES HERE
        # bot.send_before_message(sender_id)
        blocks = vendor.menu
        block = blocks['get_started']
        print(bot.send_template_message(sender_id, block))
        return "text", 200
    # elif webhook_type == "quick_reply" and helper.quick_replies_events(data) == "send_menu":
    #     m1.send(sender_id)
    #     m2.send(sender_id)
    #     m3.send(sender_id)
    #     m4.send(sender_id)
    #     m5.send(sender_id)
    #     return "Sent Menu", 200

    elif webhook_type == "quick_reply":
        # HANDLE QUICK REPLIES HERE
        # bot.send_before_message(sender_id)
        block_name = helper.quick_replies_events(data)
        blocks = vendor.menu
        if block_name in blocks:
            block = blocks[block_name]
            # bot.send_template_message(sender_id, block)
            print(bot.send_template_message(sender_id, block))

        return "quick_reply", 200

    elif webhook_type == "postback":
        # HANDLE POSTBACK HERE
        # bot.send_before_message(sender_id)
        block_name = helper.postback_events(data)

        blocks = vendor.menu
        if block_name in blocks:

            block = blocks[block_name]
            # bot.send_template_message(sender_id, block)
            print(bot.send_template_message(sender_id, block))

        return "postback", 200
    else:
        return "ok", 200
    return "ok", 200