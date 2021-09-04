import os




path_file = './personas.txt'


with open(path_file,mode='r') as f:

    for linea in f.readlines():
        print(linea)



