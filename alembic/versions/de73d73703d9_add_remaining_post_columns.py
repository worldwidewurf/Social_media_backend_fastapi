"""add remaining post columns

Revision ID: de73d73703d9
Revises: 76a088bbeae0
Create Date: 2023-06-24 17:22:59.545692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de73d73703d9'
down_revision = '76a088bbeae0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("published",sa.Boolean(),nullable=False,server_default="TRUE"))
    op.add_column("posts",sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text("now()"),nullable=False))


def downgrade() -> None:
    op.drop_column("posts","created_at")
    op.drop_column("posts","published")
