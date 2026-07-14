from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

m1 = ChatOpenAI()
m2 = ChatOpenAI() #or any other model

p1 = PromptTemplate(
    template = 'generate short and simple notes on \n {text}',
    input_variables=['text']
)

p2 = PromptTemplate(
    template = 'generate 5 short question-answer from \n {text}',
    input_variables=['text']
)

p3 = PromptTemplate(
    template = 'merge the following docs into a single doc -> \n {notes} and {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'notes': p1 | m1 | parser,
        'quiz': p2 | m2 | parser
    }
)

merge_chain = p3 | m1 | parser

chain = parallel_chain | merge_chain

text = """
 big text
"""

result = chain.invoke({'text': text})

print(result)

