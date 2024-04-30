"""empty message

Revision ID: 48363d671688
Revises: 
Create Date: 2024-04-29 09:53:08.185042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48363d671688'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exName', sa.String(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('repeat', sa.Integer(), nullable=True),
    sa.Column('setRp', sa.Integer(), nullable=True),
    sa.Column('text', sa.Integer(), nullable=True),
    sa.Column('createDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workout')
    # ### end Alembic commands ###