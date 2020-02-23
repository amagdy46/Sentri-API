"""empty message

Revision ID: b061bb7bddec
Revises:
Create Date: 2020-02-23 05:52:08.857753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b061bb7bddec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vendors', sa.Column('open_hours', sa.DateTime(), nullable=True))
    op.add_column('vendors', sa.Column('close_hours', sa.DateTime(), nullable=True))


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vendors', 'open_hours')
    op.drop_column('vendors', 'close_hours')
    # ### end Alembic commands ###
