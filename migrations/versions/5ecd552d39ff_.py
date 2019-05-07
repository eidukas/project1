"""empty message

Revision ID: 5ecd552d39ff
Revises: 
Create Date: 2019-05-07 16:58:05.345211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ecd552d39ff'
down_revision = '5ecd552d39ef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('calendar_new', sa.Column('quarterly_report', sa.Boolean))


def downgrade():
    op.drop_column('calendar_new', 'quarterly_report')
