"""empty message

Revision ID: 223e988a5d5b
Revises: 
Create Date: 2020-08-13 04:00:32.881358

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy_json import NestedMutableJson

# revision identifiers, used by Alembic.
revision = '223e988a5d5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vendors',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('created_time', sa.DateTime(), nullable=True),
                    sa.Column('uid', sa.String(), nullable=True),
                    sa.Column('comments', NestedMutableJson, nullable=True),
                    sa.Column('info', NestedMutableJson, nullable=True),
                    sa.Column('page_access_token', sa.String(), nullable=True),
                    sa.Column('fcm_token', sa.String(), nullable=True),
                    sa.Column('is_setup', sa.Boolean(), nullable=True),
                    sa.Column('opening_hours', sa.Time(), nullable=True),
                    sa.Column('closing_hours', sa.Time(), nullable=True),
                    sa.Column('page_id', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('page_id'),
                    sa.UniqueConstraint(
                        'page_id', 'id', name='unique_vendor_customers'),
                    sa.UniqueConstraint('uid')
                    )
    op.create_table('catalogs',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_time', sa.DateTime(), nullable=True),
                    sa.Column('page_id', sa.String(), nullable=True),
                    sa.Column('blocks', NestedMutableJson, nullable=True),
                    sa.Column('catgories', NestedMutableJson, nullable=True),
                    sa.Column('items', NestedMutableJson, nullable=True),
                    sa.ForeignKeyConstraint(
                        ['page_id'], ['vendors.page_id'], onupdate='CASCADE', ondelete='SET NULL'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('page_id')
                    )
    op.create_table('customers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('psid', sa.String(), nullable=True),
                    sa.Column('name', sa.String(length=80), nullable=True),
                    sa.Column('phone_number', sa.String(), nullable=True),
                    sa.Column('address', sa.String(), nullable=True),
                    sa.Column('created_time', sa.DateTime(), nullable=True),
                    sa.Column('page_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['page_id'], ['vendors.page_id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('psid'),
                    sa.UniqueConstraint(
                        'psid', 'id', name='unique_customer_orders')
                    )
    op.create_table('orders',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('number', sa.String(), nullable=True),
                    sa.Column('items', NestedMutableJson, nullable=True),
                    sa.Column('price', sa.Float(precision=3), nullable=True),
                    sa.Column('status', sa.String(), nullable=True),
                    sa.Column('is_confirmed', sa.Boolean(), nullable=True),
                    sa.Column('time', sa.DateTime(), nullable=True),
                    sa.Column('psid', sa.String(), nullable=True),
                    sa.Column('page_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['page_id'], ['vendors.page_id'], ),
                    sa.ForeignKeyConstraint(['psid'], ['customers.psid'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('number')
                    )
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('customers')
    op.drop_table('catalogs')
    op.drop_table('vendors')
    # ### end Alembic commands ###
