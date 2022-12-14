"""empty message

Revision ID: 795b3a9cd159
Revises: 6ea290e41414
Create Date: 2022-10-25 20:59:43.206542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '795b3a9cd159'
down_revision = '6ea290e41414'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teamTable',
    sa.Column('pokemon_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.pokemon_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], )
    )
    op.drop_table('team')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name='team_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='team_pkey')
    )
    op.drop_table('teamTable')
    # ### end Alembic commands ###
