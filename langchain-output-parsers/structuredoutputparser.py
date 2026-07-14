# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# # from langchain_core.output_parsers import JsonOutputParser
# from langchain_core.output_parsers import StructuredOutputParser
# from langchain.output_parsers.structured import ResponseSchema

# load_dotenv()

# model = ChatOpenAI()

# schema = [
#     ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
#     ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
#     ResponseSchema(name='fact_3', description='Fact 3 about the topic'),

# ]

# parser = StructuredOutputParser()

# t = PromptTemplate(
#     template='Give 3 facts about {topic} \n {format}',
#     input_variables=['topic'],
#     partial_variables={'format':parser.get_format_instructions()}

# )

# prompt = t.invoke({'topic':'black hole'})

# r = model.invoke(prompt)

# result = parser.parse(r)

# print(result)