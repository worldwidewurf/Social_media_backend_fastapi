"""create post table

Revision ID: 74d35ed5a858
Revises: 
Create Date: 2023-06-24 00:45:42.182914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74d35ed5a858'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",sa.Column("id",sa.Integer(),primary_key=True,nullable=False),sa.Column("title",sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_table("posts")
