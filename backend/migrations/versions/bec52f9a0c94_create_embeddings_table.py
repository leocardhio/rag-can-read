"""create embeddings table

Revision ID: bec52f9a0c94
Revises: 
Create Date: 2026-04-15 22:56:04.676614

"""
import sqlalchemy as sa
import pgai

from migrations.utils import get_url
from typing import Sequence, Union
from alembic import op
from pgai.vectorizer.configuration import (
    EmbeddingOllamaConfig, 
    ChunkingRecursiveCharacterTextSplitterConfig,
    FormattingPythonTemplateConfig,
    DestinationTableConfig
)

from config import get_settings


# revision identifiers, used by Alembic.
revision: str = 'bec52f9a0c94'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

config = get_settings()

def create_vectorizer() -> None:
    op.create_vectorizer(
        source="contexts",
        destination=DestinationTableConfig(target_table="contexts_embedding_store"),
        embedding=EmbeddingOllamaConfig(
            model="qwen3-embedding:4b",
            dimensions=1024
        ),
        chunking=ChunkingRecursiveCharacterTextSplitterConfig(
            chunk_size=500,
            chunk_overlap=50,
            separators=["\n\n", "\n", " ", ""]
        ),
        formatting=FormattingPythonTemplateConfig(template='$title - $chunk')
    )

def install_pgai() -> None:
    try:
        url = get_url(config)
        pgai.install(url)
    except Exception as e:
        print(f"Error occurred while installing pgai: {e}")
        
def uninstall_pgai() -> None:
    try:
        op.execute('DROP SCHEMA IF EXIST ai CASCADE')
        op.execute('DROP EXTENSION IF EXISTS ai')
    except Exception as e:
        print(f"Error occurred while uninstalling pgai: {e}")

def upgrade() -> None:
    """Upgrade schema."""
    op.execute('''
      CREATE TABLE IF NOT EXISTS contexts (
        id BIGSERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT NOT NULL
      )
    ''')
    install_pgai()
    create_vectorizer()
    


def downgrade() -> None:
    """Downgrade schema."""
    op.execute('DROP TABLE IF EXISTS contexts CASCADE')
    op.drop_vectorizer(target_table="contexts_embedding_store", drop_all=True)
    uninstall_pgai()
