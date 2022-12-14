"""empty message

Revision ID: a08f145320e6
Revises: 0dd0f30fda45
Create Date: 2022-10-24 23:42:08.727882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a08f145320e6'
down_revision = '0dd0f30fda45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('team', sa.Column('pokemon_id', sa.Integer(), nullable=False))
    op.add_column('team', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'team', 'pokemon', ['pokemon_id'], ['pokemon_id'])
    op.create_foreign_key(None, 'team', 'user', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'team', type_='foreignkey')
    op.drop_constraint(None, 'team', type_='foreignkey')
    op.drop_column('team', 'user_id')
    op.drop_column('team', 'pokemon_id')
    # ### end Alembic commands ###
