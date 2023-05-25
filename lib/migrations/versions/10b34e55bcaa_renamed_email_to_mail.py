"""Renamed email to mail

Revision ID: 10b34e55bcaa
Revises: 791279dd0760
Create Date: 2023-05-25 13:33:52.426411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10b34e55bcaa'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='mail')


def downgrade() -> None:
    op.alter_column('students', 'mail', new_column_name='email')
