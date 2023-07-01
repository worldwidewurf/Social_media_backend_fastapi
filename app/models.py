from .database import Base
from sqlalchemy import Column, Integer, String, Boolean,func,DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
    """Model representing a post."""

    __tablename__ = "posts"
    
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    title = Column(String,nullable=False)
    contents = Column(String,nullable=False)
    published = Column(Boolean,nullable=False,default=True)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")
      
class User(Base):
    """Model representing a user."""

    __tablename__ = "users"
    
    email = Column(String,nullable=False,unique=True)
    id = Column(Integer,primary_key=True,nullable=False)
    password = Column(String,nullable=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    phone_number = Column(String,nullable=False)

class Vote(Base):
    """Model representing a vote."""
    __tablename__ = "votes"
      
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    