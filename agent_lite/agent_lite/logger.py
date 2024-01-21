from abc import ABC, abstractmethod 


'''
    Logger will send an event object to some data store (Kafka, RDB, etc)
'''
def Logger(ABC):

    @abstractmethod  
    def log(event: Object):
        pass
