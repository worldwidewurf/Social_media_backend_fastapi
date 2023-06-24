"""add fk to post table

Revision ID: 76a088bbeae0
Revises: c4a0c03fd375
Create Date: 2023-06-24 16:29:01.338575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76a088bbeae0'
down_revision = 'c4a0c03fd375'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk",source_table="posts",referent_table="users",local_cols=["owner_id"],remote_cols=["id"],ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("post_users_fk","posts",type_="foreignkey")
    op.drop_column("posts","owner_id")
