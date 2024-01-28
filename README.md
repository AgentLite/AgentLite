# agent_lite
Lightweight, generic typings and utils for building custom agents in your app's backend. This is meant to be complementary of mainstream RAG/agent frameworks. I just don't have the time or energy to write 200+ integrations.

## Installation
You can build the project from source for now. I'll put it up on PyPi soon.

## Use Cases
- Building custom agents that you have fine-grained control over
- Using this library as a complementary extension to LlamaIndex and Langchain integrations

Like React, you can use as little or as much of this library as you'd like. Personally, I think simple structure for composable agents is sorely needed in the Generative AI space (as of early 2024).

## Basic Functionality
- Tools for LLMs to use
- Simple typings for chains of agent steps (use ```apipe()``` in ```composition.py```)
- Serializable chains of arbitrary functions (use ```cloudpickle``` to serialize, ```pickle``` to deserialize)

## How to Contribute
Haven't thought of this yet, but check the Feedback section for now.

## Feedback
Just shoot me a Linkedin message, profile here: https://www.linkedin.com/in/elliotkang7/
