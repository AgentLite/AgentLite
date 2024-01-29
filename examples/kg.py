from agent_lite import OpenAIModel, Tool, Context, Link, Prompt, apipe
from pydantic import BaseModel

#TODO: Neo4j KG store
class KGStore(BaseModel):
    #TODO: Think about whether we use the API key or the client
    api_key: str 
    def insert(entity: str, relationship: str):
        #TODO: Do this
        pass

#TODO: Context
stores = {'kg': None}
context = Context()


#TODO: Link 1: Named Entity Recognition with LLM 




#TODO: Link 2: Use prompt template to generate triplets + place into Neo4j DB







if __name__ == "__main__":
    #TODO: Execution code for simple LLM agent 
    

    #TODO: Agent workflow: Get product description JSON >> Link (Use LLM to identify entities) >> Link (Prompt template + get output from LLM + place into Neo4j DB)

    #TODO: Chain these asynchronously + serialize + deserialize + asyncio.run()

    #TODO: Do some visualization with Neo4j KG

    print("hello world")
