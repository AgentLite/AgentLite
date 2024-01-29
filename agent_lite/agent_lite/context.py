from pydantic import BaseModel
from typing import Any, Optional
from .tool import Tool


class Context(BaseModel):
    model: Optional[Any] = {}
    logger: Optional[Any]  = {} 
    stores: Optional[dict[str, Any]] = {} 
    tools: Optional[dict[str, Any]] = {}

