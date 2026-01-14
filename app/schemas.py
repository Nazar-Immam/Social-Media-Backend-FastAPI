from pydantic import BaseModel , EmailStr, conint ,Field
from datetime import datetime
from typing import Annotated

#Response model for user.
class UserResponse(BaseModel):
    email: EmailStr
    created_at: datetime
    id: int

    class Config:
        from_attributes=True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserRelationship(BaseModel):
    email: EmailStr

#Model for reponse structure
class Post(PostBase):  #inheriting the base class , that will give title,content,published
    id: int
    created_at: datetime  
    owner_id: int
    owner: UserRelationship 

    class Config:
        from_attributes = True

#Response for post with votes (joins)
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes=True


#Model to create a user
class UserCreate(BaseModel):
    email:EmailStr
    password: str




#Login credentials schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

#schema for token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: int


#model for vote table
class Vote(BaseModel):
    post_id: int
    dir:Annotated[int, Field(strict=True, le=1)]
