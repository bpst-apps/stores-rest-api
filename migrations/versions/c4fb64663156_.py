"""empty message

Revision ID: c4fb64663156
Revises: 
Create Date: 2023-02-03 21:46:42.647486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4fb64663156'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_tags')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item_tags',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('item_id', sa.INTEGER(), nullable=True),
    sa.Column('tag_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['items.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
