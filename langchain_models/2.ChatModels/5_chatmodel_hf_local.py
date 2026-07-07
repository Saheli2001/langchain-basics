from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2.5-7B-Instruct",
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=1,
        max_new_tokens=30
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the Capital of India?")

print(result.content)