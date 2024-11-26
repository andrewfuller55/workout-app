"""1

Revision ID: a9c25931074f
Revises: 
Create Date: 2024-11-14 17:42:09.183566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9c25931074f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_plans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sets', sa.Integer(), nullable=False),
    sa.Column('workout_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_plans_user_id_users')),
    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], name=op.f('fk_user_plans_workout_id_workouts')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_plans')
    op.drop_table('workouts')
    op.drop_table('users')
    # ### end Alembic commands ###
