from pydantic import BaseModel
from typing import Any, Optional
from .tool import Tool


class Context(BaseModel):
    model: Optional[Any] = None
    logger: Optional[Any]  = None 
    stores: Optional[dict[str, Any]] = None 
    tools: Optional[dict[str, Any]] = None

