"""add last few columns to post table

Revision ID: 339359971394
Revises: a17c95f8bd59
Create Date: 2026-01-17 12:05:36.104300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '339359971394'
down_revision: Union[str, Sequence[str], None] = 'a17c95f8bd59'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column(
        'published', sa.Boolean() , nullable=False , server_default='TRUE'
    ))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True) , nullable=False , server_default=sa.text('now()')
    ))

    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
