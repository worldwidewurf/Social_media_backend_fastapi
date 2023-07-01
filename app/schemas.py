
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

"""_summary_ : This module contains the schemas for the models.
they determine the structure of the data that will be sent to the client or received from the client.
"""

class PostBase(BaseModel):
    """
    Base model for a post.
    """

    
    title : str
    contents: str
    published: bool = True

class PostCreate(PostBase):
    """
    Model for creating a new post.
    Inherits from PostBase.
    """
    pass
    
class UserResponse(BaseModel):
    """
    Model for a user.
    """
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
        
class PostResponse(PostBase):

    """
    Model for a post.
    Inherits from PostBase.
    """
    id: int
    created_at: datetime
    owner_id: int 
    owner: UserResponse
    class Config:
        orm_mode = True

class PoesOut(BaseModel):
    """
    Model for a post.
    Inherits from PostBase.
    """
    
    Post: PostResponse
    votes: int 
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):

    """
    Model for creating a new user.
    """
    
    email: EmailStr
    password: str
    
class UserLogin(BaseModel):
    """
    Model for logging in a user.
    """
    email: EmailStr
    password: str
    
class Token(BaseModel):
    """
    Model for a token.
    """
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    """
    Model for token data.
    """
    id : Optional[str] = None


class Vote(BaseModel):
    """
    Model for a vote.
    """
    post_id: int
    dir: conint(le=1)
