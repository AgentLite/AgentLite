from agent_lite import OpenAIModel, Tool, Context, Link, Prompt, apipe
from pydantic import BaseModel
from typing import Callable 
import aiohttp 
import asyncio
import os

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

#Nodes: Brand, Seller, Category
nodes = ["Babolat", "Tennis Warehouse", "Tennis Racquets"]
products = [
    {
        "name": "Babolat Pure Aero 98",
        "MSRP": "$279.99",
        "Dealer Price": "$189.99",
        #The description is long, but maybe we can use MapReduce or some filtering algorithm to truncate the description 
        "Description": "Babolat adds another chapter to the most controlled and surgical member of the Pure Aero family. Formerly called the Pure Aero VS, the Pure Aero 98 gives big hitters a powerfully precise weapon. Compared to the standard Pure Aero, this racquet features a more compact head along with a denser string pattern and a thinner, more flexible beam. The payoff is extra control, which comes in handy on bigger cuts or when targeting the lines. That said, this stick still packs enough pop to put your opponent in check. For 2023 Babolat adds NF² Technology which uses flax inserts at 3/9 in the head to soften ball impact. Babolat also updates its FSI Spin technology with slightly tighter string spacing. The result is greater control (and confidence) when maximizing stroke speed in the service of power and spin. With some nice updates to the response, the Pure Aero 98 delivers the spin and power of a modern player's racquet but with the control and feel needed to fully engage with your targets."
    },
    {
        "name": "Babolat Pure Drive",
        "MSRP": "$259.99",
        "Dealer Price": "$189.99",
        "Description": "Babolat adds another chapter to the game's most iconic modern player's racquet. As with previous versions of the Pure Drive, this update keeps the same easy learning curve and explosive spec profile that has attracted generations of players. Updated with Babolat's new HTR System, the Pure Drive's graphite layup has been reengineered for higher torsional rigidity, resulting in more efficient energy transfer to the ball. To help with vibration dampening, Babolat has devoted more space in the shaft to SWX Pure Feel, a thin and extremely flexible viscoelastic rubber that sits between the racquet's carbon layers. Additional features include FSI Power Technology, which optimizes the grommet system and string spacing for higher levels of power and spin. On court, this racquet's explosive acceleration and spin-friendly targeting make it a dangerous weapon from the baseline. It also packs impressive all-court mobility, making it great for cranking winners on the run or charging into the front court and finishing points at net. With incremental tweaks to the feel, this update won't disappoint especially if you place a premium on quick handling. The Pure Drive continues to be one of the best options for those who want a light and explosive player's racquet."
    }
]
relations = ["sells", "isProductOf", "SubCategory"]

#TODO: RELATION restrictions are hard-coded to save time, but we can automate this too
kg_prompt: Prompt = lambda product, nodes, relations: '''
    Generate several triplets based on the following product description:
    {0}

    The NAME is a new node that we want to describe in relation to the current nodes. The current nodes of type <NODE<PRODUCT>> are:
    {1}
    
    Nodes of type <NODE> have subtypes. For example,
    "Babolat" is a <NODE<BRAND>>
    "Tennis Warehouse" is a <NODE<VENDOR>>
    "Tennis Racquets" is a <NODE<CATEGORY>>

    The following relationships are forbidden:
    <NODE<PRODUCT>> CANNOT map a "sells" relation to a <NODE<VENDOR>>

    Here are the available relations of type RELATION:
    {2}


    Here are some examples of the finished output:

    <Wilson RF97 Pro Staff V14, isProductOf, Wilson>
    <Head Prestige Pro 2021, SubCategory, Tennis Racquets>


    Output should be in the following format:
    ["<NAME, RELATION, NODE>", ...]
    '''.format(product, nodes, relations)

#TODO: Link 2: Use this to generate triplets
class TripletGenerator(Link):
    
    def forward(self, products: list[object], nodes: list[str], relations: list[str]):
        pass
    
    #TODO: Passing a list to a function chain will likely result in issues, make sure this is okay
    async def a_forward(self, products: list[object], nodes: list[str], relations: list[str]):
        #TODO: Finish this Link function
        predict_func: Callable = self.context.model.async_predict 
        pass

#TODO: Programmatically validate triplets. Remove the triplets that don't comply with our restrictions.
'''
For example, a <PRODUCT> should never "sell" a <VENDOR>.
Sometimes the LLM will output <"Babolat Pure Aero 98", "SELLS", "TENNIS WAREHOUSE">
'''



if __name__ == "__main__":
    #TODO: Execution code for simple LLM agent 
    print(kg_prompt(products[0], nodes, relations)) 
    
    async_session = aiohttp.ClientSession()
    async def try_this():
        async_session = aiohttp.ClientSession()
        llm_args = {
            'model': 'gpt-3.5-turbo',
            'temperature': 0.1
        }
        #Hard-coded Triplet generation
        llm = OpenAIModel(async_session = async_session, llm_args = llm_args, api_key = os.environ.get('OPENAI_API_TOKEN', ""))
        output = await llm.async_predict(kg_prompt(products[0], nodes, relations))
        print(output)
        '''
        Output:
        ["<Babolat Pure Aero 98, isProductOf, Babolat>", "<Babolat Pure Aero 98, SubCategory, Tennis Racquets>"]
        '''
        await async_session.close()

    asyncio.run(try_this())
    #TODO: Do some visualization with Neo4j KG
