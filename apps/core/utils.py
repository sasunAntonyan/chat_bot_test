import hashlib
import random
import string
import requests
from chat_bot.settings.base import KEY, WEATHER_API_KEY, KEY_1


def generate_unique_id(value, length=8):
    """
    generate id from passed value
    :param value:
    :param length: key length
    :return:
    """

    salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length)).encode(
        'utf-8')
    value = value.encode('utf-8')
    unique_key = hashlib.sha1(salt + value).hexdigest()

    return unique_key[:length]


def get_weather():
    # url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/' + KEY + '?apikey=' + WEATHER_API_KEY + '&details=true'
    # r = requests.get(url=url)
    # data = r.json()
    # weather = data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value']

    weather_to_celsius = (63 - 32) * 5/9

    return "{:0.0f}".format(weather_to_celsius)

