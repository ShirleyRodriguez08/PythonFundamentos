# guardar el archivo - control + s

lista_numeros = [1,1,2,3,4,4,5,1]

# 1. Solicito numero para particionar lista
n = int(input("Introduzca un numero de particion de la lista: "))

# 2. Particiono la lista
a = lista_numeros[:n]
b = lista_numeros[n:]
tupla_lista = (a, b)

# 3. Muestro lista particionada
print(tupla_lista)
