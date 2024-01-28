from typing import TypeVar, Callable

#Prompt is a type of function that takes arguments and returns a string
Prompt = Callable[..., str]

def simple_prompt(name: str):
    return f'Your name is {name}'


#TODO: Add basic prompts

if __name__ == '__main__':
    prompt_ref: Prompt = simple_prompt
    print(prompt_ref("John"))
    print("Hello World")
