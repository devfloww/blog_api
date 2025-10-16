from sqlalchemy import Column, Text, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID as _UUID
from uuid import UUID, uuid4

from core.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(_UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password_hash = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # relationships
    post = relationship("Post", back_populates="author", cascade="all, delete")
    comment = relationship("Comment", back_populates="users", cascade="all, delete")

class Post(Base):
    __tablename__ = "posts"

    id = Column(_UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    author_id = Column(_UUID, ForeignKey('user.id'), ondelete='CASCADE')

    # realtionships
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    

class Comment(Base):
    __tablename__ = "comments"

    id = Column(_UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user_id = Column(_UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"))
    post_id = Column(_UUID(as_uuid=True), ForeignKey("post.id", ondelete="CASCADE"))

    # Relationships
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
