from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):

    setiment: Literal['positive','Negative'] = Field(description= 'Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

p1 = PromptTemplate(
    template= 'Classify the sentiment into positive or negative \n {feedback} \n {format}',
    input_variables=['text'],
    partial_variables={'format': parser2.get_format_instructions()}
)

classifier_chain = p1 | model | parser

result = classifier_chain.invoke({'feedback': 'great movie'})

p2 = PromptTemplate(
    template='Write an appropriate response for the Positive feedback \n {feedback}',
    input_variables=['feedback']
)

p3 = PromptTemplate(
    template='Write an appropriate response for the Negative feedback \n {feedback}',
    input_variables=['feedback']
)
chain1 = p2 | model | parser
chain2 = p3 | model | parser

branch_chain = RunnableBranch(
    (lambda x:x['sentiment'] == 'positive', chain1),
    (lambda x:x['sentiment'] == 'negative', chain2),
    RunnableLambda(lambda x: 'could not find sentiment')

)

final_chain = classifier_chain | branch_chain

result = final_chain.invoke({'feedback':'bad movie'})

print(result)