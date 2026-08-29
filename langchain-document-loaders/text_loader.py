from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()
prompt = PromptTemplate(template= 'Summarize the following text: {text}', input_variables=['text'])

loader = TextLoader(r"C:\Users\E87271\Desktop\langchain_basics\langchain-document-loaders\poem.txt", encoding='utf-8')
doc = loader.load()

print(doc[0])

chain = prompt | model | parser
print(chain.invoke({'text': doc[0].page_content}))