

cantidad = int(input('Ingrese la cantidad de numeros a introducir: '))

lista_numeros = []
# solicito n veces un numero por teclado y lo añado a mi lista
for i in range(cantidad):
    numero = int(input(f'Ingrese el {i+1} numero: '))
    lista_numeros.append(numero)

sumatoria = 0
for e in lista_numeros:
    #print(f'la suma de sumatoria:{sumatoria} + e: {e}  es:{sumatoria + e}')
    sumatoria += e

print(f'la media aritmetica de los elementos es {sumatoria / cantidad}')