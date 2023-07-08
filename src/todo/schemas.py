from pydantic import BaseModel


class CreateToDo(BaseModel):
    title: str
