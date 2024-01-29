from agent_lite import Tool, Context, Link, Prompt, apipe
from pydantic import BaseModel

#TODO: Neo4j KG store
class KGStore(BaseModel):

    def insert(entity: str, relationship: str):
        #TODO: Do this
        pass

#TODO: Context



#TODO: NER tool 





#TODO: Link







if __name__ == "__main__":
    #TODO: Execution code for simple LLM agent 
    

    #TODO: Agent workflow: Get product description JSON >> Link (Use LLM to identify entities) >> Link (Prompt template + get output from LLM + place into Neo4j DB)

    #TODO: Chain these asynchronously + serialize + deserialize + asyncio.run()

    #TODO: Do some visualization with Neo4j KG

    print("hello world")
