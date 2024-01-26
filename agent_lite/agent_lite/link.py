from pydantic import BaseModel
from typing import TypeVar
from abc import abstractmethod

T = TypeVar("T")
'''
    A chain is made up of Links.
'''
class Link(BaseModel):
    context: T 

    @abstractmethod
    def forward(self):
        '''
            Main method for executing the Link in the LLM chain
        '''
        pass
    
    #TODO: In the future, we might we able to use LLMs to evaluate chains of functions.
    def backward(self):
        pass