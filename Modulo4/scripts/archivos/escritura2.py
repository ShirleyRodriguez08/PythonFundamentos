

contenido = ['nuevo\n','linea']

# en modo escritura, si archivo ya existe , se borra lo anterior y se pone data nueva
with open('./escritura1.txt',mode='w') as f:

    f.writelines(contenido)
