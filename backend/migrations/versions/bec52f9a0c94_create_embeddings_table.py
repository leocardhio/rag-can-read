"""create embeddings table

Revision ID: bec52f9a0c94
Revises: 
Create Date: 2026-04-15 22:56:04.676614

"""
import sqlalchemy as sa

from migrations.utils import get_url
from typing import Sequence, Union
from alembic import op
from pgvector import Vector

from config import get_settings


# revision identifiers, used by Alembic.
revision: str = 'bec52f9a0c94'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

config = get_settings()

def create_contexts_table() -> None:
    op.create_table(
        'contexts',
        sa.Column('id', sa.BigInteger, primary_key=True, autoincrement=True),
        sa.Column('title', sa.VARCHAR(255), nullable=False),
        sa.Column('content', sa.Text, nullable=False),
        sa.Column('embedding', Vector(1024), nullable=True)
    )
    
def drop_contexts_table() -> None:
    op.execute('DROP TABLE IF EXISTS contexts CASCADE')

def install_pgvector() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS vector')   

def uninstall_pgvector() -> None:
    op.execute('DROP EXTENSION IF EXISTS vector')

def upgrade() -> None:
    """Upgrade schema."""
    install_pgvector()
    create_contexts_table()


def downgrade() -> None:
    """Downgrade schema."""
    drop_contexts_table()
    uninstall_pgvector()
