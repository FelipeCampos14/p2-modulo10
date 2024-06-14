from pydantic import BaseModel
from typing import Optional

class BlogCreate(BaseModel):
    title: str
    content: str


class BlogPost(BlogCreate):
    id: int

    class Config:
        orm_mode = True

