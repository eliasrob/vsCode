import requests


API_KEY = "7ea40ab79d7128a10383b3c5c4b3b649"
base_url = "https://api.openweathermap.org/data/2.5/weather"

# city = input("enter city Name: ")
lat =input("enter Lat")
long =input("enter Long")
# request_url = f"{base_url}?appid={API_KEY}&q={city}"

secondUrl = f"{base_url}?lat={lat}&lon={long}&appid={API_KEY}"


response = requests.get(secondUrl)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = round(data['main']['temp'] -273.5, 2)

    print("Weather is: ", weather)
    print("Tempreature: ", temp, "celsius" )
    
else:
    print("an error occured")

