from abc import abstractmethod 
from typing import TypeVar
from pydantic import BaseModel

#Source generic try:
#TODO: Make this type more strict
S = TypeVar("S")

'''
    Logger will send an event object to some data store (Kafka, RDB, etc)
'''
class Logger(BaseModel):

    sources: S 

    @abstractmethod  
    def log(self, event: object):
        '''
        event: Event Object
        sources: Dict of sources to log to (Kafka, RDB, etc)
        '''
        pass

class PrintLogger(Logger):
    def log(self, event: object):
        #Send message to kafka 
        pass


if __name__ == "__main__":
    #TODO: Try doing this with print statements first
    logger = PrintLogger(sources = {"what": "else"})
    print(logger.log({'message': "something", 'time': "now"}))
