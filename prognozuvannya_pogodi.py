import requests


def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {

        "q": city_name,

        "appid": api_key,

        "units": "metric",  # Цельсий

        "lang": "ru"  # Русский язык

    }

    try:

        response = requests.get(base_url, params=params)

        data = response.json()

        if response.status_code == 200:

            weather = data['weather'][0]['description']

            temp = data['main']['temp']

            feels_like = data['main']['feels_like']

            humidity = data['main']['humidity']

            wind_speed = data['wind']['speed']

            print(f"Погода в {city_name}:")

            print(f"- Состояние: {weather.capitalize()}")

            print(f"- Температура: {temp}°C (ощущается как {feels_like}°C)")

            print(f"- Влажность: {humidity}%")

            print(f"- Скорость ветра: {wind_speed} м/с")

        else:

            print(f"Ошибка: {data['message']}")

    except Exception as e:

        print(f"Произошла ошибка: {e}")


# Замените <ваш_API_ключ> на ваш реальный API-ключ

api_key = "<ваш_API_ключ>"

city = input("Введите название города: ")

get_weather(city, api_key)

