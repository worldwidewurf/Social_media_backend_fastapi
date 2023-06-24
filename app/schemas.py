
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class PostBase(BaseModel):
    
    title : str
    contents: str
    published: bool = True

class PostCreate(PostBase):
    pass
    
class UserResponse(BaseModel): #post
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True
        
class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int 
    owner: UserResponse
    class Config:
        orm_mode = True

class PoesOut(BaseModel):
    Post: PostResponse
    votes: int 
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class Token(BaseModel):
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    id : Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
