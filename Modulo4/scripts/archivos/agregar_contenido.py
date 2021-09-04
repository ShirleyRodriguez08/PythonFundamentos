



# de un archivo ya existente, agrego contenido al final de este

nuevo_conteido = ['mas texto\n','mas texto de nuevo']

with open('./personas.txt',mode='a') as f:

    f.writelines(nuevo_conteido)
    print('se agrego contenido al final del archivo')