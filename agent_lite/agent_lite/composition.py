from functools import reduce
import asyncio
import inspect

#TODO: Add functional parts for higher order function serialization, etc.

#TODO: Compose synchronous functions

#This is the combinator for piping functions together
def pipe(*functions):
    return(reduce(lambda f, g: lambda *args, **kwargs: g(f(*args, **kwargs)), functions))

#We end up with a function that takes argument 'y' to call the inner function
def async_lambda(f, g):
    async def child_f(x):
        return await g(await f(x))
    return(lambda *args, **kwargs: child_f(*args, **kwargs))

def apipe(*functions):
    return(reduce(async_lambda, functions)) 

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
    #See, it still runs with asyncio.run :)
    asyncio.run(trythis())
    #TODO: Export tests to /tests folder
