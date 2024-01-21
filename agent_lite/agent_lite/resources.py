from pydantic import BaseModel



class Resource(BaseModel):
    #TODO: Add more potential resources as we move on
    num_threads: int
   


if __name__ == "__main__":
    data = Resource(num_threads = 4)
    print(data)
