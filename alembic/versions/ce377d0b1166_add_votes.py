"""add votes

Revision ID: ce377d0b1166
Revises: de73d73703d9
Create Date: 2023-06-24 17:36:35.199139

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ce377d0b1166'
down_revision = 'de73d73703d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.add_column('posts', sa.Column('contents', sa.String(), nullable=False))
    op.create_index(op.f('ix_posts_id'), 'posts', ['id'], unique=False)
    op.drop_column('posts', 'content')
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('now()'))
    op.add_column('posts', sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_posts_id'), table_name='posts')
    op.drop_column('posts', 'contents')
    op.drop_table('votes')
    # ### end Alembic commands ###
