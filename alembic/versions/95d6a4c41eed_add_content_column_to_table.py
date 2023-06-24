"""add content column to table

Revision ID: 95d6a4c41eed
Revises: 74d35ed5a858
Create Date: 2023-06-24 00:55:17.980599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95d6a4c41eed'
down_revision = '74d35ed5a858'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column("posts","content")
    pass
