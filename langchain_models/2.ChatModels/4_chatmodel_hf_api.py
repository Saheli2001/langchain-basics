from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# import os

# HF_TOKEN = os.getenv("HF_TOKEN")
load_dotenv()

# print(os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    temperature=1
)
model = ChatHuggingFace(llm=llm)

result = model.invoke('make a three line poem')
print(result.content)