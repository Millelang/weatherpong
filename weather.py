import requests


def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
    else:
        print("City not found.")
    return temperature

def main():
    city = input("Enter city name: ")
    api_key = "a20313f627478d6c32a64c6aaf78365b"
    get_weather(city, api_key)


if __name__ == "__main__":
    main()


def get_feeling():
    city = input("Enter city name: ")
    api_key = "a20313f627478d6c32a64c6aaf78365b"
    temp = get_weather(city, api_key)
    temp = round(temp)
    if temp >= 30:
        WHITE = (139, 64, 0)
        return WHITE
    elif temp >= 20:
        WHITE = (204, 85, 0)
        return WHITE
    elif temp >= 0 :
        WHITE = (255, 255, 255)
        return WHITE
    elif temp < 0:
        WHITE = (0,0,255)
        return WHITE
