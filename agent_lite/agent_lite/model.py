from abc import ABC, abstractmethod

'''
    Agent Model, takes queries and returns outputs in String format.
'''

class LLM(ABC):
    @abstractmethod 
    def predict(query: str) -> str:
        pass
