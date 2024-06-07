import requests
import os
import json
import random
import time
if not os.path.exists('Avatars_Prueba'):
    os.makedirs('Avatars_Prueba')
numpost=input("Ingrese la cantidad de posts(Entre 5 y 500)(-1 para salir): ")
if numpost=="-1":
    print('saliendo...')
if numpost.isdecimal():
    numpost=int(numpost)
    if numpost >= 5 and numpost <= 500:
        print(f"Creando {numpost} posts...")
        posts=[]
        for i in range(int(numpost)):
            json_url=f'https://jsonplaceholder.typicode.com/users/{i+1}'
            response=requests.get(json_url)
            data=response.json()
            data['Bienvenida_al_Usuario']=f"Bienvenido {data['name']}!"
            estilos=['bottts', 'initials','big-ears', 'micah', 'avataaars', 'pixel-art']
            print("Elegir un estilo")
            for index, estilo in enumerate(estilos, start=1):
                print(f"{index}. {estilo}")
            opcion=input("Seleccione el numero correspondiente al estilo deseado: ")
            while not opcion.isdecimal() or int(opcion) not in range(1, len(estilos)+1):
                print("Por favor, ingresar un numero valido: ")
            estilo_elegido=estilos[int(opcion)-1]
            avatar_url=f"https://api.dicebear.com/8.x/{estilo_elegido}/svg?seed={data['name']}"
            data['avatar']=avatar_url
            url_image=f"https://picsum.photos/{random.randint(1, 1000)}"
            data['Imagen']=url_image
            tiempo=time.strftime('%d/%m/%Y %H:%M:%S')
            data['Hora_actual']=f"La hora actual es {tiempo}"
            posts.append(data)
            with open('./Avatars_Prueba/post.json', 'w') as f:
                json.dump(posts, f)
            print("Archivos guardados en Avatars_Prueba")
    else:
        print("El numero que ingreso esta fuera del rango (5, 500)")
else: 
    print("No se ingreso un numero decimal")