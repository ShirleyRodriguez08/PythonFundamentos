import os

listado = ['lina1\n','linea2\n','linea3\n','linea4']

with open('file2.txt',mode='w') as f:
    f.writelines(listado)