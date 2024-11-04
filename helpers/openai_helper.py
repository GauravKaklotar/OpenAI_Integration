from openai import OpenAI
from config.config import Config
import json
import time

client = OpenAI(
    api_key=Config.OPENAI_API_KEY,
)

def get_weather(city):
    weather_data = {
        "New York": "Sunny, 25 degrees Celsius.",  
        "London": "Cloudy, 18 degrees Celsius.",
        "Paris": "Rainy, 16 degrees Celsius."
    }
    return weather_data.get(city, "Weather data not available for this location.")

def get_openai_response(prompt):
    functions = [
        {
            "name": "get_weather",
            "description": "Retrieve weather information for a specified city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to get the weather information for"
                    }
                },
                "required": ["city"]
            }
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions about weather information."},
            {"role": "user", "content": prompt}
        ],
        functions=functions,
        function_call="auto"
    )

    assistant_message = response.choices[0].message

    if assistant_message.function_call:
        function_name = assistant_message.function_call.name
        arguments = json.loads(assistant_message.function_call.arguments)

        if function_name == "get_weather":
            city = arguments["city"]
            # Get weather information
            weather_info = get_weather(city)

            # Create the function call response message
            function_call_result_message = {
                "role": "assistant",
                "content": f"The weather in {city} is: {weather_info}."
            }

            new_messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"The weather in {city} is: {weather_info}. Can you explain this to the user?"},  
                assistant_message,  
                function_call_result_message 
            ]

            final_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=new_messages
            )

            final_assistant_message = final_response.choices[0].message.content
            return final_assistant_message
    else:
        return assistant_message.content
    

def test_streaming():
    start_time = time.time()

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'user', 'content': 'Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'}
        ],
        temperature=0,
        stream=True  
    )

    collected_chunks = []
    collected_messages = []

    for chunk in response:
        chunk_time = time.time() - start_time  
        collected_chunks.append(chunk)  
        chunk_message = chunk.choices[0].delta.content  
        collected_messages.append(chunk_message) 
        print(f"Message received {chunk_time:.2f} seconds after request: {chunk_message}") 

    print(f"Full response received {chunk_time:.2f} seconds after request")

    collected_messages = [m for m in collected_messages if m is not None]
    full_reply_content = ''.join(collected_messages)
    print(f"Full conversation received: {full_reply_content}")

    return full_reply_content