import requests
import time
import json
import os
if not os.path.exists('JSONcarpeta'):
    os.makedirs('JSONcarpeta')
else:
    print("JSONcarpeta already exists")
url_image='https://picsum.photos/200/300'
image_response=requests.get(url_image)
cantidad_posts = input('Ingrese la cantidad de posts (tiene que ser entre 1 y 10.000): ')
if not cantidad_posts.isdigit() or int(cantidad_posts) < 1 or int(cantidad_posts) > 10000:
    print('Se ingreso un número fuera de rango o no se ingresó un número válido')
else:
    for i in range(1, int(cantidad_posts) + 1):
        response=requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')
        if response.status_code == 200:
            data=response.json()
            data['hora actual']=time.strftime("%d/%m/%Y, %H:%M:%S")
            image_url = image_response.url
            data['imagen']=image_url
            data["title"]="Esto si puede estar pasando mi loco"
            print(f'El post {i} se ha obtenido con éxito')
            print(data)
            with open(f'./JSONcarpeta/posts.json', 'w') as f:
                json.dump(data, f)
        else:
            print(f'Error al obtener el post {i}')
        print('Todos los post se guardaron en posts.json')