
### User model ###

from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: Optional[str]
    code: Optional[str]
    description: Optional[str]
    stock: Optional[str]
    value: Optional[str]
    altcode: Optional[str]
