import requests


class Weather:
    def __init__(self, token, url):
        self.token = token
        self.url = url

    def is_response_good(self, res):
        if 200 <= res.status_code < 300:
            return True

    def get_city_weather(self, city_name, lang, units):
        query = {
            "q": city_name,
            "appid": self.token,
            "lang": lang,  # "ru"
            "units": units  # "metric"
        }
        response = requests.get(self.url, params=query)

        if not self.is_response_good(response):
            return "Случилась ошибка, повторите попытку еще раз"

        res = response.json()

        description = res['weather'][0]['description']
        temp = res['main']['temp']

        return_str = f"В городе {city_name} {description}\n" \
                     f"Температура воздуха {temp} градусов"

        return return_str


city_name = input("Введите название города: ")
lang = input("Введите язык, на котором необходимо вывести информацию (например, ru): ")
units = input("Введите единицы измерения, в которых необхоимо вывести данные (например, metric): ")
token = "799461e6591f3a6352bc3ef6727ecd2b"
url = "https://api.openweathermap.org/data/2.5/weather"

open_weather = Weather(token, url)
print(open_weather.get_city_weather(city_name, lang, units))
