import requests
import pyperclip
import json

url='https://jsonplaceholder.typicode.com/posts/1'
response=requests.get(url)
data=response.json()
titulo=data['title']
contenido=data['body']
with open('post.txt', 'w') as file:
    file.write(f"Titulo: {titulo}\n\n Contenido:{contenido}")
    print('Datos guardados en post.txt')
with open('post.txt', 'r') as file:
    texto=file.read()
    pyperclip.copy(texto)

print("Contenido copiado en el portapapeles")