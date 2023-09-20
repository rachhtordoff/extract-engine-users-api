"""empty message

Revision ID: 52c10f0560b5
Revises: 7afb44c77607
Create Date: 2023-09-20 20:09:34.541166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52c10f0560b5'
down_revision = '7afb44c77607'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=40),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('code',
               existing_type=sa.VARCHAR(length=40),
               nullable=False)

    # ### end Alembic commands ###