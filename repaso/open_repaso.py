with open('texto.txt', 'w') as file:
    file.write('Hola!')
with open('texto.txt', 'r') as file:
    contenido=file.read()
    print(contenido)