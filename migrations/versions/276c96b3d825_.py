"""empty message

Revision ID: 276c96b3d825
Revises: 3c0f7218617d
Create Date: 2024-03-02 08:47:03.037490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '276c96b3d825'
down_revision = '3c0f7218617d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('console',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('time_slot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('time_slot')
    op.drop_table('game')
    op.drop_table('console')
    # ### end Alembic commands ###