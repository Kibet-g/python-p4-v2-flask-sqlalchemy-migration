"""Add department and hire_date fields to Employee model

Revision ID: c28ecc077d90
Revises: 9ec900d000cd
Create Date: 2025-01-19 20:13:54.226350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c28ecc077d90'
down_revision = '9ec900d000cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('department', sa.String(), nullable=False))
    op.add_column('employees', sa.Column('hire_date', sa.Date(), nullable=False))
    op.alter_column('employees', 'salary',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'salary',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('employees', 'hire_date')
    op.drop_column('employees', 'department')
    # ### end Alembic commands ###
