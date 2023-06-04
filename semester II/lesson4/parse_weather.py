import requests


def parse_weather(city: str):
    api_key = '0ebe025b8d93f180657fa5a4ccf33ba7'
    url = f'https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}'
    response = requests.get(url)

    return response.json()



if __name__ == '__main__':
    print(parse_weather('Kyiv'))
    # city = input('Enter your city: ')
    # weather = parse_weather(city)['main']
    # temp = weather['temp'] - 273.15
    # print(f'City - {city}\nTemperature - {temp}')