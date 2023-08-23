from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///password_manager.db")

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)

    categories = relationship("Category", back_populates="user")
    entries = relationship("Entry", back_populates="user")

    def __repr__(self):
        return (
            f"User {self.id} "
            + f"{self.username}, "
            + f"{self.password}, "
            + f"{self.email} "
        )


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="categories")
    entries = relationship("Entry", back_populates="category")

    def __repr__(self):
        return f"Category {self.id} " + f"{self.name}, " + f"{self.user_id} "


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    website = Column(String, nullable=False)
    username = Column(String)
    password = Column(String, nullable=False)
    notes = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    user = relationship("User", back_populates="entries")
    category = relationship("Category", back_populates="entries")
    tags = relationship("Tag", secondary="entry_tags", back_populates="entries")

    def __repr__(self):
        return (
            f"Entry {self.id} "
            + f"Website: {self.website}, "
            + f"Username: {self.username} "
            + f"Password: {self.password} "
            + f"Note: {self.notes} "
            + f"Creation date: {self.created_at} "
            + f"Update date: {self.updated_at} "
        )


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    entries = relationship("Entry", secondary="entry_tags", back_populates="tags")


# Many to many relationship: an entry can have many tags, and a tag can be associated with many entries
entry_tags = Table(
    "entry_tags",
    Base.metadata,
    Column("entry_id", Integer, ForeignKey("entries.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)
