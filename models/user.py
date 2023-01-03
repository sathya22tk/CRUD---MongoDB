from typing import Optional

from pydantic import BaseModel


class Course(BaseModel):
    id: int
    name: str
    description: str
    level: str
    requirements: str
    instructor: str
    ratings: int
    price: int
