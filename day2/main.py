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
        "role": "system", "content": """
                    You are a careful kitchen assistant who scales recipes.

                    You work ONE STEP PER RESPONSE. Each response must contain exactly one
                    step and nothing else. Never write the next step in the same response.
                    After you write a step, stop. The user will reply "Continue" and you
                    then write only the next step.

                    The steps, in order:

                    Step 1: Restate the original servings and the target servings.
                    Step 2: Calculate the scale factor (target / original).
                    Step 3: Multiply each ingredient by the factor, showing each calculation.
                    Step 4: Round sensibly (whole eggs, practical measures) and say what you rounded.
                    Step 5: Check by working backward from one scaled ingredient.
                    Final Answer: the scaled ingredient list.

                    Rules:
                    - Start every response with its label, for example "Step 3:".
                    - Only write "Final Answer:" after Step 5 is done, and write nothing after it.
                    - Do not ask the user anything. Do not skip steps, even for easy recipes.
                    - Use plain text only, no markdown.
                """
    }]
while user_input.lower() != "exit":
    user_input = input("-> ")
    message_history.append({"role": "user", "content": user_input})
    final_answer = ""
    for _ in range(6):  # Loop for 6 steps (5 steps + final answer)
        stream = client.chat.completions.create(
            model="gemini-3.6-flash",
            messages=message_history,
            stream=True,
            temperature=0,
            top_p=0.9,
        )
        message = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                message += chunk.choices[0].delta.content
        message_history.append({"role": "assistant", "content": message})
        
        # Check if the message contains "Final Answer:"
        if "Final Answer:" in message:
            final_answer = message
            break
        print(message, flush=True) 
    print(final_answer)  # Print a newline after the response
    message_history.append({"role": "assistant", "content": final_answer})
    
    
# user - User Input - Query
# assistant - Previous AI response - Context
# system -  Guidelines

