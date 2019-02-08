"""empty message

Revision ID: 5ecd552d39df
Revises: 
Create Date: 2019-02-08 15:14:03.844841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ecd552d39df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('isbn', sa.String(length=20), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author', sa.String(length=255), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('calendar',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Industry', sa.Text(), nullable=True),
    sa.Column('Date', sa.DateTime(), nullable=True),
    sa.Column('Ticker', sa.Text(), nullable=True),
    sa.Column('Event', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('reviews_id', sa.Integer(), nullable=False),
    sa.Column('reviews_content', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('reviews_id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('reviews')
    op.drop_table('calendar')
    op.drop_table('books')
    # ### end Alembic commands ###