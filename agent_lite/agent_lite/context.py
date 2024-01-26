from pydantic import BaseModel

class Context(BaseModel):
    model: Any #This should be a Model object
    logger: Any #This should be a Logger object 
    resources: Any #This should be a Resource object 
    stores: Any #This should be a Stores object
