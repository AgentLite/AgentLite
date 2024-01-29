from pydantic import BaseModel
from typing import Any, Optional
from .tool import Tool


class Context(BaseModel):
    models: Optional[dict[str, Any]] = {} 
    loggers: Optional[dict[str, Any]] = {} 
    stores: Optional[dict[str, Any]] = {} 
    tools: Optional[dict[str, Any]] = {}

