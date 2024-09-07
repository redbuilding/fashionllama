# 🌦️👗👕 FashionLlama

This application uses Ollama and local model Llama 3.1 8B to provide real-time weather information and fashion advice using an AI agent.
The app demonstrates use of Ollama function calling to use WeatherAPI.com. It recommends appropriate, family-friendly clothing based on current weather conditions.

## Features

- Fetches real-time weather data using the [WeatherAPI](https://www.weatherapi.com/).
- Interacts with Llama 3.1 8B via Ollama to dynamically call functions.
- Provides detailed weather information including temperature, wind speed, humidity, and air quality index (AQI).
- Offers fashion recommendations for men and women based on the current weather.
- Ensures all recommendations are safe for work (family-friendly).

## Prerequisites

1. **Python**: Ensure Python 3.x is installed on your machine. You can download it [here](https://www.python.org/downloads/).
2. **WeatherAPI Key**: Sign up for a free API key at [WeatherAPI.com](https://www.weatherapi.com/).
3. **Ollama**: Ensure Ollama’s Python SDK is installed and configured to use the `llama3.1` model.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/redbuilding/fashionllama.git
   cd fashionllama
   ```

2. **Set up the virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   Install the required Python libraries listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root and add your `WEATHER_API_KEY` and base URL:
   ```bash
   WEATHER_API_KEY=your_weatherapi_key_here
   WEATHER_BASE_URL=https://api.weatherapi.com/v1/current.json
   ```

5. **Run the application**:
   ```bash
   python3 app.py  #On Windows: python app.py
   ```

## Usage

1. When prompted, enter the name of the city for which you want to retrieve the weather:
   ```bash
   Enter the name of the city to check the weather: Nome, AK
   ```

2. The application will fetch and display real-time weather information including temperature (in Fahrenheit), wind speed, humidity, and AQI.

## Example Output

```bash
Weather report: Weather in Nome, United States of America: Light rain, 48.4°F, wind: 17.4 mph, humidity: 81%, AQI (US EPA): 2

Fashion Recommendation:
Given the weather conditions in Nome, I would recommend the following family-friendly attire:

For Men:

* A lightweight rain jacket or windbreaker to protect against the light rain and 17.4 mph winds.
* Moisture-wicking base layer (such as a thermal top) to keep you dry and comfortable under the outer layer.
* Waterproof pants or leggings are not necessary, but you may want to consider wearing water-resistant jeans or trousers for added protection.
* A breathable, moisture-wicking hat and gloves will help keep your head and hands warm in the cold and windy conditions. Look for waterproof or water-resistant materials to ensure dryness.
* Comfortable, closed-toe shoes with good traction are essential for walking on potentially wet surfaces.

For Women:

* A lightweight rain jacket or windbreaker is a great starting point, as it will keep you dry and comfortable in the light rain.
* Consider wearing a breathable, moisture-wicking base layer (such as a thermal top) to help regulate your body temperature under the outer layer.
* Water-resistant leggings or pants are not necessary, but water-repellent tights or leggings can be helpful for added protection against wind and rain.
* A warm and breathable hat, such as a beanie or a scarf, will help keep your head and neck cozy in the cold and windy conditions. Look for moisture-wicking materials to ensure dryness.
* Comfortable, closed-toe shoes with good traction are essential for walking on potentially wet surfaces.

General Tips:

* Dress in layers to stay warm and comfortable in case the temperature fluctuates throughout the day.
* Choose breathable, moisture-wicking fabrics that will help keep you dry and comfortable.
* Consider adding a scarf or neck gaiter for added warmth and protection against wind and rain.
* Don't forget to pack extra clothing items, such as socks and gloves, in case they get wet.

These recommendations should provide suitable attire for men and women to wear on this drizzly day in Nome while still being safe for work and suitable for all ages.
```

## Logging

The application uses logging to provide detailed information about tool execution and potential errors. Logs can be found in the terminal or output window.

## Development

If you'd like to contribute or modify this project, feel free to fork the repository and make pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
