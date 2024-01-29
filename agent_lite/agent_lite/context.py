from pydantic import BaseModel
from typing import Any
from .tool import Tool


class Context(BaseModel):
    model: Any #This should be a Model object
    logger: Any #This should be a Logger object 
    stores: Any #This should be a Stores object
    tools: dict[str, Tool]


