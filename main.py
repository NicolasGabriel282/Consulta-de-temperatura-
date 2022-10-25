
import requests
from pprint import pprint

api_key = '6c069b75e6bd9f32ca4b261b69ace993'
cidade= input('Digite o nome da cidade:')

base_url = 'https://api.openweathermap.org/data/2.5/weather?appid='+api_key +'&q='+cidade

informacoes =requests.get(base_url).json()
temp=(float(informacoes['main']['temp']))
temperatura= temp - 273.15
print(f'Temperatura em {cidade} é de {temperatura:,.2f}°C')