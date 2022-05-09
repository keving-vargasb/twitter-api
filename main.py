# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional, List

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# FastAPI
from fastapi import FastAPI, status

app = FastAPI()

# Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(..., min_length=8, max_length=64)

class User(UserBase):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

## Users
@app.post(path="/signup", response_model=User, status_code=status.HTTP_201_CREATED, summary="Register a user", tags=["Users"])
def signup():
    pass

@app.post(path="/login", response_model=User, status_code=status.HTTP_200_OK, summary="Login a user", tags=["Users"])
def login():
    pass

@app.get(path="/users", response_model=List[User], status_code=status.HTTP_200_OK, summary="Ger all users", tags=["Users"])
def show_all_users():
    pass

@app.get(path="/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK, summary="Get a user", tags=["Users"])
def get_user():
    pass

@app.delete(path="/users/{user_id}/delete", response_model=User, status_code=status.HTTP_200_OK, summary="Delete a user", tags=["Users"])
def delete_user():
    pass

@app.put(path="/users/{user_id}/update", response_model=User, status_code=status.HTTP_200_OK, summary="Update a User", tags=["Users"])
def update_user():
    pass


## Tweets
@app.get(path="/", response_model=List[Tweet], status_code=status.HTTP_200_OK, summary="Get all tweets", tags=["Tweets"])
def get_all_tweets():
    pass

@app.post(path="/post", response_model=Tweet, status_code=status.HTTP_201_CREATED, summary="Post a tweets", tags=["Tweets"])
def post_tweet():
    pass