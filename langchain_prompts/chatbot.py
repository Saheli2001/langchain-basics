from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano", max_tokens=3000, reasoning_effort="low")

chat_history = [SystemMessage(content="You are a helpful assistant.")]

while True:
    user_input = input("You : ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ', result.content)

print(chat_history)