import requests
import ollama
import os
from dotenv import load_dotenv
import logging

# Step 1: Load environment variables
load_dotenv()
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_BASE_URL = os.getenv('WEATHER_BASE_URL')

# Step 2: Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Step 3: Define the actual tool function that will call WeatherAPI.com to get real-time weather
def get_current_weather(city):
    # Build the complete API request URL with city and API key
    request_url = f"{WEATHER_BASE_URL}?key={WEATHER_API_KEY}&q={city}&aqi=yes"

    logging.debug(f"Requesting weather for {city} with URL: {request_url}")

    # Make a request to the WeatherAPI.com API
    response = requests.get(request_url)

    if response.status_code == 200:  # 200 means the request was successful
        weather_data = response.json()  # Parse the JSON response

        # Extract important information from the API response
        location = weather_data['location']
        current = weather_data['current']
        condition = current['condition']['text']
        temperature_f = current['temp_f']
        wind_mph = current['wind_mph']
        humidity = current['humidity']
        air_quality = current['air_quality']
        aqi_us_epa = air_quality['us-epa-index']

        # Format the weather information to return to the model
        weather_report = (f"Weather in {location['name']}, {location['country']}: "
                          f"{condition}, {temperature_f}°F, wind: {wind_mph} mph, "
                          f"humidity: {humidity}%, AQI (US EPA): {aqi_us_epa}")
        logging.debug(f"Weather report: {weather_report}")
        return weather_report
    else:
        logging.error(f"Error fetching weather data: {response.status_code}")
        return f"Sorry, couldn't fetch weather data for {city}. Please check the city name."

# Step 4: Define the tool for Ollama to call (function calling configuration)
weather_tool = {
    'type': 'function',
    'function': {
        'name': 'get_current_weather',
        'description': 'Get the current weather for a city',
        'parameters': {
            'type': 'object',
            'properties': {
                'city': {
                    'type': 'string',
                    'description': 'The name of the city',
                },
            },
            'required': ['city'],
        },
    },
}

# Step 5: Define the interaction with Ollama's model using actual function calling
def interact_with_model(city_name):
    response = ollama.chat(
        model='llama3.1',  # Use the Llama model
        messages=[
            {'role': 'user', 'content': f"What is the weather in {city_name}?"}  # User's input
        ],
        tools=[weather_tool],  # Provide the tool to the model
    )

    # Check if a tool call was requested by the model
    if 'tool_calls' in response['message']:
        tool_calls = response['message']['tool_calls']
        logging.debug(f"Tool calls received: {tool_calls}")

        for tool_call in tool_calls:
            function_name = tool_call['function']['name']
            arguments = tool_call['function']['arguments']

            # Execute the tool if the model requested 'get_current_weather'
            if function_name == 'get_current_weather' and 'city' in arguments:
                city = arguments['city']
                logging.debug(f"Executing function '{function_name}' with arguments: {arguments}")
                return get_current_weather(city)
            else:
                logging.error(f"Unknown function requested: {function_name}")
                return f"Error: Unknown function requested - {function_name}"
    else:
        logging.error("No tool call received from the model.")
        return "Error: No tool call received."

# Step 6: Ask the model to act as a fashion consultant based on the weather
def get_fashion_recommendation(weather_report):
    # Send a new request to Ollama asking for fashion recommendations based on the weather
    fashion_prompt = (f"The following is the weather report:\n\n{weather_report}\n\n"
                      "Based on this, please recommend appropriate, family-friendly attire for men and women "
                      "to wear today. Ensure the recommendations are safe for work and appropriate for all ages.")

    response = ollama.chat(
        model='llama3.1',
        messages=[
            {'role': 'system', 'content': 'You are a helpful fashion consultant.'},
            {'role': 'user', 'content': fashion_prompt}
        ]
    )

    # Return the fashion recommendation provided by the model
    return response['message']['content']

# Step 7: Ask the user to input a city name
city_name = input("Enter the name of the city to check the weather: ")

# Step 8: Send the user's request to the model and let it handle the tool calling
weather_report = interact_with_model(city_name)

# Step 9: Get a fashion recommendation based on the weather
if weather_report.startswith("Sorry"):
    print(weather_report)  # Print the error if the weather couldn't be fetched
else:
    print(f"Weather result: {weather_report}")

    # Get the fashion recommendation and print it
    fashion_recommendation = get_fashion_recommendation(weather_report)
    print("\nFashion Recommendation:")
    print(fashion_recommendation)
