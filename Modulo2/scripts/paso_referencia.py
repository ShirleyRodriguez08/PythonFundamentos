

def funcion_lista(my_lista):
    my_lista[0] = 90 + my_lista[0]
    return my_lista


lista_numeros = [1,2,3]

print(lista_numeros) #[1,2,3]
print(funcion_lista(lista_numeros)) # [91 , 2 , 3]
print(lista_numeros) # [91, 2, 3]

print(funcion_lista(lista_numeros)) # [181, 2, 3]
print(lista_numeros) # [181, 2, 3]