import requests
import time
import json
cantidad_posts = input('Ingrese la cantidad de posts (tiene que ser entre 1 y 10.000): ')
if not cantidad_posts.isdigit() or int(cantidad_posts) < 1 or int(cantidad_posts) > 10000:
    print('Se ingreso un número fuera de rango o no se ingresó un número válido')
else:
    post=[]
    for i in range(1, int(cantidad_posts) + 1):
        response=requests.get(f'https://jsonplaceholder.typicode.com/posts/{i}')
        if response.status_code == 200:
            data=response.json()
            data['hora actual']=time.strftime("%d/%m/%Y, %H:%M:%S")
            post.append(data)
            print(f'El post {i} se ha obtenido con éxito')
            print(data)
            with open(f'posts{i}.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        else:
            print(f'Error al obtener el post {i}')
        print('Todos los post se guardaron en posts.json')