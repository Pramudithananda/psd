import pyowm

# Initialize the PyOWM library with your API key
owm = pyowm.OWM('YOUR_API_KEY')

# Get the user's location
location = input("Enter your city or zip code: ")

# Search for the location in the OpenWeatherMap database
try:
    observation = owm.weather_at_place(location)
    weather = observation.get_weather()
    temperature = weather.get_temperature('fahrenheit')['temp']
    description = weather.get_detailed_status()
    print("The temperature in " + location + " is " + str(temperature) + " degrees Fahrenheit.")
    print("The weather is " + description + ".")
except:
    print("Sorry, we couldn't find the weather for that location.")
