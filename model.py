from typing import Optional
from pydantic import BaseModel


class DataModel(BaseModel):
    id: int
    
