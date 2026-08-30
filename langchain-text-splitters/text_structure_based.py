from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Users\E87271\Desktop\langchain_basics\langchain-document-loaders\Resnet.pdf")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=0,
    separator = '')

result = splitter.split_documents(docs)

print(result[1].page_document)