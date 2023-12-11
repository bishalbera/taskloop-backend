from datetime import datetime
from pydantic import BaseModel


class Task(BaseModel):
    id: str
    name: str
    description: str
    deadline: datetime
   
