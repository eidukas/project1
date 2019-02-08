"""empty message

Revision ID: 5ecd552d39ef
Revises: 
Create Date: 2019-02-09 16:52:03.844841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ecd552d39ef'
down_revision = '5ecd552d39df'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('calendar_new',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Industry', sa.Text(), nullable=True),
    sa.Column('Date', sa.DateTime(), nullable=True),
    sa.Column('Ticker', sa.Text(), nullable=True),
    sa.Column('Event', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calendar_new')
    # ### end Alembic commands ###
