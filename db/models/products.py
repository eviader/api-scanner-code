
### User model ###

from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: str | None
    code: str
    description: str
    stock: str
    value: str
    altcode: str
