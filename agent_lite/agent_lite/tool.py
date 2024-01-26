from pydantic import BaseModel
from abc import abstractmethod
from typing import Callable

class Tool(BaseModel):
    '''
        desc: Tool description
        execute: Function that executes this tool
    '''
    desc: str
    
    @abstractmethod 
    def use(self):
        pass

class PlusTool(Tool):
    desc: str = "A function that takes two <Number> arguments (a, b) and returns a + b" 

    #Example Tool 
    def use(self, a, b):
        return a + b 



if __name__ == "__main__":
    plus_tool = PlusTool()
    print(plus_tool.use(1, 2))
