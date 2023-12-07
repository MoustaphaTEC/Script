"""two-factor authentication

Revision ID: c971946af9c5
Revises: d0a540aa85e0
Create Date: 2021-03-18 18:36:32.377549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c971946af9c5'
down_revision = 'd0a540aa85e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('verification_phone', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'verification_phone')
    # ### end Alembic commands ###
