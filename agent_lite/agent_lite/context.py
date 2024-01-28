from pydantic import BaseModel
from typing import Any

class Context(BaseModel):
    model: Any #This should be a Model object
    logger: Any #This should be a Logger object 
    stores: Any #This should be a Stores object
