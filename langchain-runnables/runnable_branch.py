from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(template= 'Generate a report: {topic}',
                    input_variables=['topic'],
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(template= 'Summarize: {topic}',
                    input_variables=['topic'],
)
report_gen_chain = RunnableSequence(prompt1, model, parser)
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, report_gen_chain),
    RunnablePassthrough()
)
final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic': 'AI'}))