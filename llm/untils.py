from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def model_to_llm(model:str=None):
        llm = Ollama(model=model)
        return llm

def chat(llm, question):
    output_parser = StrOutputParser()
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个对话助手，可以回答我提出的问题，但要求问题不能超过50个字符，且不能包含特殊字符"),
        ("user", "{input}")
    ])
    chain = prompt | llm | output_parser
    response = chain.invoke({"input": question})
    return response