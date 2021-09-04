import os


# abriendo un archivo

path_file = './personas.txt'

# forma1
with open(path_file,mode='r',encoding='utf-8') as f:
    # leyendo contenido de archivo
    # print(f.read()) # lee todo el archivo como string

    print(f.readlines()) # devuelve una lista en la cual cada linea es un elemento de la lista

# forma 2
# file =  open(path_file,mode='r')
# print(file.read())
# file.close() # cierro archivo


