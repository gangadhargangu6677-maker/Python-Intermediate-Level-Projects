import requests  # Importing the requests library to make HTTP requests

# Ask the user to enter the city name
city_name = input("Enter city name: ") 

# Your API key from OpenWeatherMap (replace with your own if needed)
api_key = "b8bec54da1c481bfc946c024a1004ec1"

# Construct the API URL
# Note: Corrected "unites" → "units" and set to "metric" for Celsius
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&unites=metric"

# Send a GET request to the API
response = requests.get(url)

# Check if the response is successful (status code 200 means OK)
if response.status_code == 200:
  # Convert the response data into JSON format
  weather_data = response.json()

  # Print weather details
  print(f"Weather in {city_name}")
  print("Temperature:", weather_data['main']['temp'], "C")
  print("Feels like:", weather_data['main']['feels_like'], "C")
  print("Humidity:", weather_data['main']['humidity'], "%")
  print("Condition:", weather_data['weather'][0]['description'])
else:
  # If city is not found or API fails Error handling 
  print("City you enter not found!")
