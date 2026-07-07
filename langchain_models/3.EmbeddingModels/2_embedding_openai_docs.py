from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",
                 dimensions=32) #depends on cost

documents = ["Delhi is the Capital of India",
             "Kolkata is the Capital of West Bengal",
             "Mumbai is the Capital of Maharashtra",]
result = embedding.embed_documents(documents)

print(str(result))