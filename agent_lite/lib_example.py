
from agent_lite import Resource

def basic_node(context):
    def chain_action(statement):
        print(context)
    return chain_action

if __name__ == "__main__":
    resource_obj = Resource(num_threads = 4)
    basic_node(resource_obj)("Something") 
    print("hello world!") 
