from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

p1 = PromptTemplate(
    template='Generate a detailed report on {topic} ',
    input_variables=['topic']
)

p2 = PromptTemplate(
    template='Generate 5 pointer summary on {text} ',
    input_variables=['text']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = p1 | model | parser | p2 | model | parser

result = chain.invoke({'topic':'AI'})

print(result)