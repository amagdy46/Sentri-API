import datetime
from enum import unique
from uuid import uuid1
from app import db
from sqlalchemy_json import NestedMutableJson
from ..models.bot import Bot


class Catalog(db.Model):
    __tablename__ = 'catalogs'
    __table_args__ = (db.UniqueConstraint(
        'uuid', 'id', name='unique_catalog_categories'),)
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.DateTime)
    uuid = db.Column(db.String, unique=True)
    page_id = db.Column(db.String, db.ForeignKey(
        'vendors.page_id', ondelete='SET NULL', onupdate="CASCADE"), unique=True, nullable=True)
    blocks = db.Column(NestedMutableJson)
    categories = db.relationship(
        'Category', backref='catalog', lazy='select')

    def __init__(self, page_id):
        self.page_id = page_id
        self.uui = uuid1().hex
        self.blocks = {
            'main_menu': {
                'payload': {
                    'template_type': 'generic',
                    'elements': []
                }
            },
        }
        self.created_time = datetime.datetime.utcnow()
        # self.knowledge = {
        #     'greetings': {
        #         'label': 'Greetings',
        #         'values':
        #             {
        #                 'Welcome_Message':
        #                 'Welcome How Can I help you?',
        #                 'Thank_You': 'Thank You'
        #             }
        #     },
        #     'browse': {
        #         'label': 'Browse',
        #         'values': {'Order_Confirmation_Message': 'Order is Confirmed',
        #                    'Business_Closed_Message': 'Business is Closed',
        #                    'Info_Message': 'Address and Phone Number'}
        #     },

        #     'persistant_menu': {
        #         'label': 'Persistant Menu',
        #         'values':
        #             {'Show_Menu': 'Show Menu',
        #              'Show_Current_Order': 'Show Current Order'},

        #     },
        #     'buttons': {
        #         'label': 'Buttons',
        #         'values':
        #             {'Show_Info': 'Show Info',
        #              'Show_Sub_Menu': 'Sub Menu',
        #              'Show_Main_Menu': 'Main Menu',
        #              'Confirm_Order': 'Confirm Order',
        #              'Edit_Order': 'Edit Order',
        #              'Add_to_Order': 'Add to Order',
        #              'Cancel_Order': 'Cancel Order',
        #              'Track_Order': 'Track Order'
        #              }
        #     }
        #
    # Class Methods

    @classmethod
    def find_by_page_id(cls, page_id):
        return cls.query.filter_by(page_id=page_id).first()

    def set_get_started(self):
        # bot = Bot(page_access_token)
        temp = {
            'payload': {
                'template_type': 'generic',
                'elements': [
                    {
                        'title': 'Hello',
                        'image_url': '',
                        'subtitle': '',
                        'buttons': [{
                            'type': 'postback',
                            'title': 'Show Menu',
                            'payload': 'main_menu'
                        },
                            {
                            'type': 'postback',
                                    'title': 'Show Info',
                                    'payload': 'info'
                        }]

                    }
                ]
            }
        }
        self.blocks['get_started'] = temp
        print(self.blocks)
        self.save()

    def set_persistant_menu(self, page_access_token):
        bot = Bot(page_access_token)
        bot.set_persistent_menu({
            'persistent_menu': [
                {
                    'locale': 'default',
                    'composer_input_disabled': False,
                    'call_to_actions': [
                        {
                            'type': 'postback',
                            'title': 'Menu',
                            'payload': 'main_menu'
                        },
                        {
                            'type': 'postback',
                            'title': 'Current Order',
                            'payload': 'main_menu'
                        },
                        {
                            'type': 'web_url',
                            'title': 'Powered By Sentri',
                            'url': 'https://www.sentri.io/',
                        }
                    ]
                }
            ]
        })
        self.save()

    # Categories Methods

    # def add_category(self, title, subtitle, img):
    #     if len(self.blocks['main_menu']['payload']['elements']) == 13:
    #         print('Categories exceeded max capacity')
    #         return 'Categories Full'
    #     _id = uuid1().hex
    #     self.blocks[temp['id']] = {
    #         'payload': {
    #             'template_type': 'generic',
    #             'elements': []
    #         }
    #     }
    #     self.categories[_id] = temp
    #     self.build_main_menu()
    #     self.save()

    # def remove_category(self, _id):
    #     self.categories.pop(_id, None)
    #     self.build_main_menu()
    #     self.save()

    # def edit_category(self, category):
    #     if category['id'].isnumeric():
    #         category['id'] = uuid1().hex
    #     category['block'] = self.make_category_block(
    #         category['id'], category['title'], category['subtitle'], category['img'])
    #     self.categories[category['id']] = category
    #     self.build_main_menu()
    #     self.save()

    # Items Methods

    # def add_item(self, category_id, title, subtitle, price, img, in_stock):

    #     self.items[_id] = temp
    #     self.build_category(category_id)
    #     self.save()

    # def remove_item(self, _id):
    #     item = self.items[_id]
    #     self.items.pop(_id, None)
    #     if item['category_id'] in self.categories:
    #         self.build_category(item['category_id'])
    #     self.save()

    # def edit_item(self, item):
    #     if item['id'].isnumeric():
    #         item['id'] = uuid1().hex
    #     item['block'] = self.make_item_block(
    #         item['id'], item['title'], item['subtitle'], item['price'], item['img'])
    #     self.build_category(item['category_id'])
    #     self.items[item['id']] = item
    #     self.save()

    # Knowledge Methods

    # def edit_knowledge_value(self, category, key, value, page_access_token):
    #     for k, v in self.knowledge[category]['values'].items():
    #         if k == key:
    #             self.knowledge[category]['values'][k] = value
    #     if category == 'persistent_menu':
    #         self.set_persistant_menu(page_access_token)
    #     if category == 'greetings':
    #         self.set_get_started()
    #     self.build_blocks()
    #     self.save()

    # Default Model Methods

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return self

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.remove(self)
        db.session.commit()

    # Menu Building Methods
    # def build_main_menu(self):
    #     temp = []
    #     print(self.categories.items())
    #     for k, v in self.categories.items():
    #         if v['id'] in self.blocks and self.blocks[v['id']]['payload']['elements'] is not None:
    #             print(k)
    #             print(v)
    #             if 'block' not in v:
    #                 v['block'] = self.mitemsake_category_block(
    #                     v['id'], v['title'], v['subtitle'], v['img'])
    #             temp.append(
    #                 v['block'])

    #     self.blocks['main_menu']['payload']['elements'] = temp

    # def build_category(self, _id):
    #     temp = []
    #     category = self.categories[_id]
    #     for k, v in self.items.items():
    #         print(v)
    #         if v['category_id'] == _id and v['in_stock']:
    #             v['block'] = self.make_item_block(
    #                 v['id'], v['title'], v['subtitle'], v['price'], v['img'])
    #             temp.append(
    #                 v['block'])
    #     self.blocks[_id]['payload']['elements'] = temp

    # Block building functions

    # def build_blocks(self):
    #     self.set_get_started()
    #     self.build_main_menu()
    #     for title, category in self.categories.items():
    #         self.build_category(category['id'])
