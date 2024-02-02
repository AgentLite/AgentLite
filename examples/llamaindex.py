from llama_index.llms import OpenAI
from agent_lite import pipe
import os

#Output function
def format_response(completion_response):
    return completion_response.text

if __name__ == "__main__":
    #Do something
    llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo", api_key = os.environ.get("OPENAI_API_TOKEN", "")) 
    
    func_chain = pipe(llm.complete, format_response)
    print(func_chain("Hello!"))
