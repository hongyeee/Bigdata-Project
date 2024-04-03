import requests
import json

apikey = {"token"}
cities = ["Seoul,KR", "Tokyo,JP","New York,US"]

api = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
k2c = lambda k: k -273.15

for city in cities:
    url = api.format(city=city, apikey=apikey)
    response = requests.get(url)
    data = json.loads(response.text)
    city_name = city.split(",")
    print("+CITY = " + city_name[0])
    weather = data['weather'][0]['description'] 
    min_temp = k2c(data['main']['temp_min'])
    max_temp = k2c(data['main']['temp_max'])
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    deg = data['wind']['deg']
    speed = data['wind']['speed']
    print("| WEATHER = " + weather)
    print("| MIN TEMP = "+str(min_temp))
    print("| MIN TEMP = "+str(max_temp))
    print("| WEATHER = " + str(humidity))
    print("| WEATHER = " + str(pressure))
    print("| WEATHER = " + str(deg))
    print("| WEATHER = " + str(speed))

