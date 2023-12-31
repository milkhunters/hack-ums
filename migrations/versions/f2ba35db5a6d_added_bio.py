"""added bio

Revision ID: f2ba35db5a6d
Revises: e6384eb0395d
Create Date: 2023-10-20 22:06:54.871763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2ba35db5a6d'
down_revision: Union[str, None] = 'e6384eb0395d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.VARCHAR(length=255), nullable=True))
    op.alter_column('users', 'first_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('users', 'last_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=32), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.alter_column('users', 'last_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('users', 'first_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
