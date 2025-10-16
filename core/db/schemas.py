from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    password: str
    email: EmailStr

class UserOut(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    content: str

class PostOut(BaseModel):
    id: UUID
    title: str
    content: str
    created_at: datetime
    author: UserOut

    class Config:
        orm_mode = True

class CommentCreate(BaseModel):
    content: str

class CommentOut(BaseModel):
    id: UUID
    content: str
    created_at: datetime
    user_id: UserOut
    post_id: PostOut

    class Config:
        orm_mode = True

