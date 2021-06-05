# control + n - > abro un nuevo file
# control + s -> guardar cambios


# Terminal: cls -> limpiar terminal
# ejecutar python : python nombre_archivo.py

# 1. Solicitando numero
x = int(input('Por favor ingrese un dato numerico: '))

# 2. elevando numero al cubo
potencia = x ** 3

# 3. Mostrando resultado
# print('El numero elevado al cubo es : ' + str(x))

# print(f'El numero {x} elevado al cubo es: {potencia}')

print('El numero {} elevado al cubo es: {}'.format(x, potencia))
