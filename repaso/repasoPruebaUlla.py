"""1- Crear un Input que reciba INT entre 1 y 1000
a. INPUT
b. IF (INT entre 1 y 1000)

2- Importar Módulos (Requests, etc)

3- Para cada número del INPUT (numposts):
a. Extraer el Post de una URL
b. Procesar el JSON
c. Agregar una key con la fecha y hora actual
d. Agregar una key con el link de una imagen random (usar otra API - PICSUM)

4- Guardar todos los Posts en 1 JSON en la PC"""
import requests
import json
import time
import os
import random


if not os.path.exists('Repaso_Prueba'):
    os.makedirs('Repaso_Prueba')
numposts=input("Ingrese la cantidad de posts a crear(1 a 1000) (Aprete -1 para salir): ")
if numposts == '-1':
    print("saliendo...")

else:
    if numposts.isdecimal():
        numposts=int(numposts)
        print("Ingrese un valor entre 1 y 1000")
        if numposts >= 1 and numposts <= 1000:
            print(f"Creando {numposts} posts...")
        
            posts=[]
            for i in range(int(numposts)):
                url=f"https://jsonplaceholder.typicode.com/posts/{i+1}"
                response=requests.get(url)
                post=response.json()
                post['hora_actual']=time.strftime('%d/%m/%Y %H:%M:%S')
                imagen_url=f"https://picsum.photos/{random.randint(1, 1000)}"
                post['Imagen']=imagen_url
                post['body']="Este mensaje se auto destruira en 10 segundos."
                post['title']="Esto esta pasando mi loco"
                posts.append(post)
                print(posts)
            with open('./Repaso_Prueba/post.json', 'w') as f:
                json.dump(posts, f)
            print('Archivos guardados correctamente en Repaso_Prueba')