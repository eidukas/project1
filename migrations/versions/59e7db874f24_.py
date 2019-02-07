"""empty message

Revision ID: 59e7db874f24
Revises: e9be86c9dd8b
Create Date: 2019-02-07 17:36:32.264123

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '59e7db874f24'
down_revision = 'e9be86c9dd8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('sqlite_sequence')
    # op.add_column('calendar', sa.Column('Event', sa.Text(), nullable=True))
    # op.alter_column('calendar', '\xa0Event', nullable=True, new_column_name='Event')
    # op.add_column('calendar', sa.Column('id', sa.Integer(), nullable=False))
    # op.drop_column('calendar', '\xa0Event')
    op.drop_constraint('ix_users_email', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.drop_constraint('ix_users_username', 'users', type_='unique')
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.create_unique_constraint('ix_users_username', 'users', ['username'])
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('ix_users_email', 'users', ['email'])
    # op.alter_column('calendar', 'Event', nullable=True, new_column_name='\xa0Event')
    # op.add_column('calendar', sa.Column('\xa0Event', sa.TEXT(), nullable=True))
    # op.drop_column('calendar', 'id')
    # op.drop_column('calendar', 'Event')
    # op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)

    # ### end Alembic commands ###