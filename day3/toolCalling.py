import json
from openai import OpenAI


# Tool:
#   - Function is a function that a model can use to perform a specific task that it can't itself.




client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a given city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["city"]
            }
        }
    }
]

# 2. The real function
def get_weather(city, unit="celsius"):
    return json.dumps({"city": city, "temperature": 22, "unit": unit, "condition": "Sunny"})

# 3. Start conversation
messages = [{"role": "user", "content": "What's the weather in Tokyo?"}]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

msg = response.choices[0].message
messages.append(msg)

# 4. If the model wants to call a tool, run it and loop back
if msg.tool_calls:
    for call in msg.tool_calls:
        args = json.loads(call.function.arguments)
        result = get_weather(**args)
        messages.append({
            "role": "tool",
            "tool_call_id": call.id,
            "content": result
        })

    final = client.chat.completions.create(model="gpt-4o", messages=messages, tools=tools)
    print(final.choices[0].message.content)
else:
    print(msg.content)