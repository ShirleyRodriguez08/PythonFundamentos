# 1. Importacion de librerias

# 2. Defino constantes

# 3. Funciones

# 4. Mi programa

# 1. Solicito cantidad de numeros
cantidad_numeros = int(input('Ingrese la cantidad de numeros a introducir: '))

# 2. Solicito al usuario que ingrese los numeros
lista_numeros = []
for i in range(cantidad_numeros):
    x = float(input(f'Ingrese el numero {i+1}: '))
    lista_numeros.append(x)

# realizo la suma de los numeros
suma_lista = 0
for num in lista_numeros:
    suma_lista += num
suma_lista

# calculo la media aritmetica
media_aritmetica = suma_lista/cantidad_numeros

# imprimo resultado
print(f'La media Aritmetica de los elementos es {media_aritmetica}')