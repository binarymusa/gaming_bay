"""empty message

Revision ID: ef3c53f02fc6
Revises: 07e440f48b67
Create Date: 2024-03-02 09:23:49.327309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef3c53f02fc6'
down_revision = '07e440f48b67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('time_slot', schema=None) as batch_op:
        batch_op.drop_index('id')
        batch_op.create_unique_constraint(None, ['start_time'])
        batch_op.create_unique_constraint(None, ['end_time'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('time_slot', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.create_index('id', ['id'], unique=True)

    # ### end Alembic commands ###