from abc import abstractmethod
from pydantic import BaseModel
from typing import Dict, TypeVar, Optional, AsyncIterable
import requests
import asyncio
import aiohttp
import os 

'''
    Agent Model, takes queries and returns outputs in String format.
'''

#Generic LLM args & message types
A = TypeVar("A")
M = TypeVar("M")

class LLM(BaseModel):
    async_session: Optional[aiohttp.ClientSession] = None
    http_session: Optional[requests.Session] = None
    api_key: Optional[str] = None
    llm_args: Optional[dict[str, A]] = None

    class Config:
        arbitrary_types_allowed = True

    @abstractmethod 
    def predict(query: str, message_history: Optional[list[M]] = []) -> str:
        pass

    @abstractmethod
    async def async_predict(query: str, message_history: Optional[list[M]] = []) -> str:
        pass
    
    #TODO: Write streaming version

class OpenAI(LLM):
    '''
        Example LLM using OpenAI's GPT models
    '''
    
    def predict(self, query: str, message_history: Optional[list[M]] = []) -> str:
        #Make curl request to OpenAI endpoint
        headers = {"Authorization": f"Bearer {self.api_key}"}  
        prompt = {'role': 'user', 'content': query}
        response = self.http_session.post(
            'https://api.openai.com/v1/chat/completions', headers=headers, json={**self.llm_args,
                                                                                 'messages': message_history + [prompt]}
        )
        response.raise_for_status()
        message_history.append(prompt)
        response_str = response.json()["choices"][0]["message"]["content"].strip()
        message_history.append({'role': 'user', 'content': response_str})
        return response_str
    
    #TODO: Test the async side out 
    async def async_predict(self, query: str, message_history: Optional[list[M]] = []) -> str:
        
        #Make curl request to OpenAI endpoint
            headers = {"Authorization": f"Bearer {self.api_key}"}  
            prompt = {'role': 'user', 'content': query}
            response = await self.async_session.post(
            'https://api.openai.com/v1/chat/completions', headers=headers, json ={**self.llm_args,
                                                                                    'messages': message_history + [prompt]}
            )
            message_history.append(prompt)
            response_str =  (await response.json())["choices"][0]["message"]["content"].strip()
            message_history.append({'role': 'user', 'content': response_str})
            return response_str

#Trying out the implementation with raw curl requests to OpenAI
if __name__ == "__main__":
    async def try_this():
        llm_args = {
            'model': 'gpt-3.5-turbo',
            'temperature': 0.1
        }
        session = requests.Session()
        async_session = aiohttp.ClientSession()
        llm = OpenAI(http_session = session, async_session = async_session, llm_args = llm_args, api_key = os.environ.get('OPENAI_API_TOKEN', ""))
        message_history = []

        #TODO: Try Async predict
        await llm.async_predict("Hello!", [])
        await async_session.close()
    asyncio.run(try_this())
