"""First migration

Revision ID: 41215f0554e2
Revises: 
Create Date: 2024-09-08 03:44:23.208124

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '41215f0554e2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('nm_id', sa.Integer(), nullable=False),
    sa.Column('current_price', sa.Integer(), nullable=True),
    sa.Column('sum_quantity', sa.Integer(), nullable=True),
    sa.Column('quantity_by_sizes', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('product_photo_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('nm_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
