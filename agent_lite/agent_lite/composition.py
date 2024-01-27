from functools import reduce
import asyncio
import inspect
import dill

#TODO: Add functional parts for higher order function serialization, etc.


#TODO: Compose synchronous functions
def pipe(*functions):
    return(reduce(lambda f, g: lambda x: g(f(x)), functions))

#TODO: Compose async functions

async def async_pipe(*functions):
    return

def async_lambda(f, g):
    async def child_f(x):
        return await g(await f(x))
    return(lambda x: child_f(x))

def apipe(*functions):
    return(reduce(async_lambda, functions)) 


#TODO: Unroll higher-order recursive functions to make them serializable


#TODO: Serialize any function





#TODO: Testing Grounds
async def plus1(x):
    print("PLEASE")
    print(x)
    return x + 1
async def print1(x):
    print(x)
    print("CHECK CONCURRENCY")
    return x + 1
async def print2(x):
    print("Hello")
    return



if __name__ == "__main__":
    #TODO: Run mini-experiments on testing these
    async def trythis():
        exp = apipe(plus1, print1)
        print(inspect.iscoroutinefunction(exp))
        print(await exp(2))
        return
    #print(apipe(plus1, print1))

    #See, it still runs with asyncio.run :)
    asyncio.run(apipe(plus1, print1, print2)(1))
    #TODO: Export tests to /tests folder
