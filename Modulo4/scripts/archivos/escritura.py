



lineas = ['linea1\n', 'linea2\n', 'hola']


with open('./escritura1.txt',mode='w') as f:

    f.writelines(lineas)
    print('se realizó la escritura del archivo')