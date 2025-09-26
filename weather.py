import requests
import os

api_key = os.getenv("WEATHER_API_KEY")

class AllInfo:
	def __init__(self, data):
		self.city = data['location']['name']
		self.region = data['location']['region']
		self.country = data['location']['country']
		self.temp_farenheit = data['current']['temp_f']
		self.temp_celsius = data['current']['temp_c']
		self.condition = data['current']['condition']['text']
		self.precipitation = data['current']['precip_in']

	def weather_displayer(self):
		print(f"Weather is being taken from {self.city}, {self.region}, {self.country}")
		print(f"Temperature in \nFarenheit:{self.temp_farenheit}\nCelsius: {self.temp_celsius}")
		print(f"Condition is {self.condition} with precipitation amount of {self.precipitation}")

def weather_grab(location):
	response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={main_location}&aqi=no")
	data = response.json()
	return AllInfo(data)

main_location = input("Enter where the weather shall be taken from. Examples: London, New York, Lebanon, or ZIP codes(ZIP codes are most accurate)\n")
weather = weather_grab(main_location)
weather.weather_displayer()