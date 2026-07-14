from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI()

parser = JsonOutputParser()

t1 = PromptTemplate(template= 'give me name, age and city of a fictional person {topic}',
                    input_variables=['topic'],
                    partial_variables={'topic':parser.get_format_instructions()})

prompt = t1.format()

result = model.invoke(prompt)

print(parser.parse(result.content))

