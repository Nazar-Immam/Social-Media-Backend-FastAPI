"""add content column to posts table

Revision ID: a074dc0348db
Revises: 173710cc53ec
Create Date: 2026-01-17 10:43:24.736633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a074dc0348db'
down_revision: Union[str, Sequence[str], None] = '173710cc53ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts' , sa.Column('content' , sa.String() , nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
