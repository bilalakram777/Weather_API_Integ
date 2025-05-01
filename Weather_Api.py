import requests

# Function to fetch weather data from WeatherAPI.com
def fetch_weather(city, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"  # Optional: Set to "yes" if you want air quality data
    }

    try:
        # Make a GET request to the API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)

        # Parse the JSON response
        data = response.json()

        # Extract relevant information
        city_name = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        weather_description = data["current"]["condition"]["text"]

        # Display the weather information
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except KeyError:
        print("Error: Unable to fetch weather data. Please check the city name or API key.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function
def main():
    print("Welcome to the Weather App!")
    city = input("Enter the name of the city: ")
    api_key = input("Enter your WeatherAPI.com API key: ")

    # Fetch and display weather data
    fetch_weather(city, api_key)

if __name__ == "__main__":
    main()
