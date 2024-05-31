import requests
api_key='7f7823df03eab28a20f57e6bb596ba2f'
base_url='https://api.openweathermap.org/data/2.5/weather'
city=input('Ingrese el nombre de la ciudad: ')
units=input('Ingrese la unidad a usar(C para celsius, F para fahrenheit): ').upper()
if units == 'C':
    units='metric'
elif units == 'F':
    units='imperial'
else:
    print('Unidad no valida use C o F')
complete_url=f"{base_url}?q={city}&units={units}&appid={api_key}&lang=es"
print(complete_url)
response=requests.get(complete_url)
data=response.json()
def display_weather(data):
    city=data['name']
    temp=data['main']['temp']
    pressure=data['main']['pressure']
    humidity=data['main']['humidity']
    print(f"La ciudad elegida es: {city}")
    print(f"La temperatura es: {temp}")
    print(f"La presion es: {pressure}")
    print(f"La humedad es de {humidity}%")
print(display_weather(data))