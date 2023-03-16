"""Add messages model

Revision ID: 69f53977c034
Revises: 0c4e7e01dc8c
Create Date: 2023-02-19 14:56:58.958332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69f53977c034'
down_revision = '0c4e7e01dc8c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###