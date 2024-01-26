from abc import ABC, abstractmethod 


'''
    Logger will send an event object to some data store (Kafka, RDB, etc)
'''
class Logger(ABC):

    @abstractmethod  
    def log(event: Object, sources: Object):
        '''
        event: Event Object
        sources: Dict of sources to log to (Kafka, RDB, etc)
        '''
        pass

class PrintLogger(Logger):
    def log({'message': "something", 'time': "now"}, sources: {'kafka': None}):
        #Send message to kafka 
        pass


if __name__ == "__main__":
    #TODO: Try doing this with print statements first
