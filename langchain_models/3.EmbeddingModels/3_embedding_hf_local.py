from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text = "Delhi is the Capital of India"
documents = ["Delhi is the Capital of India",
             "Kolkata is the Capital of West Bengal",
             "Mumbai is the Capital of Maharashtra",]
result = embedding.embed_documents(documents)
# result = embedding.embed_query(text)

print(str(result))