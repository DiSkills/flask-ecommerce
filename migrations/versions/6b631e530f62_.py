"""empty message

Revision ID: 6b631e530f62
Revises: 4304b4ec280c
Create Date: 2021-05-31 16:07:59.128766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b631e530f62'
down_revision = '4304b4ec280c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('permission', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'permission')
    # ### end Alembic commands ###
