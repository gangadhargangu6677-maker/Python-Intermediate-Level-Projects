import requests 

city_name = "Bengaluru"
api_key = "b8bec54da1c481bfc946c024a1004ec1"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&unites=metric"


response = requests.get(url)
if response.status_code == 200:
  data = response.json()
  print("weather is ", data["weather"][0]["description"])
  print("weather temparatur is ", data["main"]["temp"])
  print("weather temparatur feels like is ", data["main"]["feels_like"])
  print("weather humidity is ", data["main"]["humidity"])