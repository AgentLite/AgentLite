from functools import reduce, partial
from agent_lite import Context
from pydantic import BaseModel

#TODO: Turn context's type into agent_lite.Context type later
def basic_node(context: BaseModel):
    def chain_action(statement):
        print(1)
        return context
    return chain_action

def basic_node2(context: BaseModel):
    def chain_action(statement, arg2):
        print(2)
    return chain_action

#Writing a combinator + functools.reduce to pipe functions
#This is also known as a combinator in lambda calculus
def pipe(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


if __name__ == "__main__":
    #Then we can try chaining these two
    #1. Define the chain 
    chain_dict = {
        1: basic_node,
        2: basic_node2
    }
    #2. Insert Context 
    #Alternatively, we can do this with a list as well
    #chain_dict = {k: v(resource_obj) for k, v in chain_dict.items()}
    chain_dict[2] = partial(chain_dict[2], arg2 = 1)
    #3. Pipe functions
    #chain_dict[2](chain_dict[1]("HEllo"))
    composed_chain = pipe(*chain_dict.values())
    
    #This should print "context" argument twice
    composed_chain("Hello?")
    print("hello world!") 
