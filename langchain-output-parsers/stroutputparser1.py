from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

t1 = PromptTemplate(template= 'write a report on {topic}',
                    input_variables=['topic'])

t2 = PromptTemplate(template= 'write a 5 line sumary on the following text. \n {text}',
                    input_variables=['text'])

parser = StrOutputParser()

chain = t1 | model | parser | t2 | model | parser

r = chain.invoke({'topic':'blackhole'})

print(r)