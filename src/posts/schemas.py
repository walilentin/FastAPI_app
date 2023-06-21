from pydantic import BaseModel


class CreatePost(BaseModel):
    title: str
    body: str
