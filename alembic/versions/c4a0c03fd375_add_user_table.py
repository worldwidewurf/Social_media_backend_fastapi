"""add user table

Revision ID: c4a0c03fd375
Revises: 95d6a4c41eed
Create Date: 2023-06-24 01:03:30.975662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4a0c03fd375'
down_revision = '95d6a4c41eed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id",sa.Integer(),primary_key=True),
                    sa.Column("email",sa.String(),nullable=False),
                    sa.Column("password",sa.String(),nullable=False),
                    sa.Column("created_at",sa.TIMESTAMP(timezone=True),server_default=sa.text("now()") ,nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email"))


def downgrade() -> None:
    op.drop_table("users")
