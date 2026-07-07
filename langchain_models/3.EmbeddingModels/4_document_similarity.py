from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = ["Virat Kohli is one of the most successful batsmen in modern cricket and has captained the Indian team across formats.",
"Rohit Sharma is known for his elegant batting style and holds the record for the highest individual score in One Day Internationals.",
"Jasprit Bumrah is regarded as one of the world's best fast bowlers because of his unique bowling action and deadly yorkers.",
"Ben Stokes is a world-class all-rounder who has played several match-winning innings for England in both Tests and limited-overs cricket.",
"Babar Azam is widely admired for his consistent batting performances and technically sound stroke play across all formats."]

query = "tell me about Virat Kohli."

doc_embeddings = embedding.embed_documents(documents)
query_embed = embedding.embed_query(query)

scores = cosine_similarity([query_embed], doc_embeddings)[0]
# print(scores)

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
print(documents[index])
