from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatOpenAI()

t1 = PromptTemplate(tamplate= 'write a report on {topic}',
                    input_variables=['topic'])

t2 = PromptTemplate(tamplate= 'write a 5 line sumary on the following text. /n {text}',
                    input_variables=['text'])

p1 = t1.invoke({'topic':'black hole'})
result = model.invoke(p1)

p2 = t2.invoke({'text':result.content})

result1 = model.invoke(p1)
