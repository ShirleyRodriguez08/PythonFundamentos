

mod_linea2= '2;Pedro;Heredia;26/12/1873\n'

# modificaremos el archivo personas.txt
with open('./personas.txt',mode='r+') as f:
    data = f.readlines()

    # modifico la linea 2
    data[1] = mod_linea2

    # retorno puntero a posicion inicial
    f.seek(0)
    f.writelines(data)

    pass