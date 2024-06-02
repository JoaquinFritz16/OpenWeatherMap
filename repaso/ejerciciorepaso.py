import requests
import pyperclip
import json
import webbrowser
import os
url='https://jsonplaceholder.typicode.com/posts/1'
response=requests.get(url)
data=response.json()
titulo=data['title']
contenido=data['body']
directorio_post='post'
filename=os.path.join(directorio_post, 'post.txt')
if not os.path.exists(directorio_post):
    os.makedirs(directorio_post)
if os.path.exists(filename):
    os.remove(filename)
with open(filename, 'w') as file:
    file.write(f"Titulo: {titulo}\n\n Contenido:{contenido}")
    print('Datos guardados en post.txt')
with open(filename, 'r') as file:
    texto=file.read()
    pyperclip.copy(texto)
webbrowser.open(f"file:///{filename}")
print("Contenido copiado en el portapapeles y archivo abierto en el navegador")