"""Initial Tables

Revision ID: ahf3432345b6
"""

from typing import Tuple

import sqlalchemy as sa
from alembic import op
from sqlalchemy import func

revision = "ahf3432345b6"
down_revision = None
branch_labels = None
depends_on = None


def create_updated_at_trigger() -> None:
    op.execute(
        """
    CREATE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS
    $$
    BEGIN
        NEW.updated_at = now();
        RETURN NEW;
    END;
    $$ language 'plpgsql';
    """
    )


def timestamps() -> Tuple[sa.Column, sa.Column]:
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
    )


def create_users_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("date_of_birth", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("phone_number", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("email", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("address", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("salt", sa.Text, nullable=False),
        sa.Column("hashed_password", sa.Text),
        sa.Column("pet_owner", sa.Boolean, nullable=False, default=False),
        sa.Column("admin", sa.Boolean, nullable=False, default=False),
        sa.Column("block", sa.Boolean, nullable=False, default=False),
        sa.Column("photo", sa.Text),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_user_modtime
            BEFORE UPDATE
            ON users
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )

def create_announcement_table() -> None:
    op.create_table(
        "announcement",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="SET NULL")),
        sa.Column("title", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=False),
        sa.Column("start_date",sa.TIMESTAMP(timezone=True), server_default=func.now()),
        sa.Column("end_date",sa.TIMESTAMP(timezone=True)),
        sa.Column("block", sa.Boolean),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_announcement_modtime
            BEFORE UPDATE
            ON announcement
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )


def create_tags_table() -> None:
    op.create_table(
        "tags", 
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id", ondelete="SET NULL")),
    )


def create_tags_for_announcement_table() -> None:
    op.create_table(
        "tags_for_announcement",
        sa.Column("announcement_id",sa.Integer, sa.ForeignKey("announcement.id", ondelete="CASCADE"),nullable=False),
        sa.Column("tag_id",sa.Integer, sa.ForeignKey("tags.id", ondelete="CASCADE"), nullable=False),
    )
    op.create_primary_key(
        "pk_tags_for_announcement", "tags_for_announcement", ["announcement_id", "tag_id"]
    )

def create_comments_table() -> None:
    op.create_table(
        "comments",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("announcement_id",sa.Integer, sa.ForeignKey("announcement.id", ondelete="CASCADE"),nullable=False),
        sa.Column("user_id",sa.Integer,sa.ForeignKey("users.id", ondelete="CASCADE"),nullable=False),
        sa.Column("content", sa.Text, nullable=False),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_comment_modtime
            BEFORE UPDATE
            ON comments 
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )

def create_pets_table() -> None:
    op.create_table(
        "pets",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("user_id",sa.Integer,sa.ForeignKey("users.id", ondelete="SET NULL"),nullable=False),
        sa.Column("date_of_birth", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("breed", sa.Text, nullable=True),
        sa.Column("preferences", sa.Text, nullable=True),
        *timestamps(),
    )


def create_pets_for_announcement_table() -> None:
    op.create_table(
        "pets_for_announcement",
        sa.Column("announcement_id",sa.Integer, sa.ForeignKey("announcement.id", ondelete="SET NULL"),nullable=False),
        sa.Column("pet_id",sa.Integer,sa.ForeignKey("pets.id", ondelete="SET NULL"),nullable=False),
    )
    op.create_primary_key(
        "pk_pets_for_announcement", "pets_for_announcement", ["announcement_id", "pet_id"]
    )

def upgrade() -> None:
    create_updated_at_trigger()
    create_users_table()
    create_announcement_table()
    create_tags_table()
    create_tags_for_announcement_table()
    create_comments_table()
    create_pets_table()
    create_pets_for_announcement_table()


def downgrade():
    op.drop_table("pets_for_announcement")
    op.drop_table("pets")
    op.drop_table("comments")
    op.drop_table("tags_for_announcement")
    op.drop_table("tags")
    op.drop_table("announcement")
    op.drop_table("users")
    op.execute("DROP FUNCTION update_updated_at_column")
