from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3-opus-20241217")

result = model.invoke("Hello, how are you?")

print(result)