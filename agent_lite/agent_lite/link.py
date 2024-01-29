from pydantic import BaseModel
from typing import TypeVar
from abc import abstractmethod

T = TypeVar("T")
'''
    A chain is made up of Links.
'''
class Link(BaseModel):
    #TODO: Add union type for Union(Context | dict[str, Any])
    context: T 

    @abstractmethod
    def forward(self):
        '''
            Main method for executing the Link in the LLM chain
        '''
        pass

    async def a_forward(self):
        '''
            Main method for executing the Link in the LLM chain
        '''
        pass
