from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
) 

user_input = ""
message_history = [
    {
        "role": "system", "content": "You are a friendly assistant that helps users with their queries. Please provide clear and concise answers."
    }
]
while user_input.lower() != "exit":
    user_input = input("-> ")
    message_history.append({"role": "user", "content": user_input})
    stream = client.chat.completions.create(
        model="gemini-3.5-flash",
        messages=message_history,
        stream=True,
        temperature=0,
        top_p=0.9,
    )
    message = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            message += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()  # Print a newline after the response
    message_history.append({"role": "assistant", "content": message})
    
    
# user - User Input - Query
# assistant - Previous AI response - Context
# system -  Guidelines

