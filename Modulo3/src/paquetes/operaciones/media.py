

def media_aritmetica(cantidad_numeros):
    lista_numeros = []
    for i in range(cantidad_numeros):
        numero = int(input(f'Ingrese el {i+1} numero: '))
        lista_numeros.append(numero)
    
    sumatoria = 0
    for e in lista_numeros:
        sumatoria += e
        
    return sumatoria / cantidad_numeros