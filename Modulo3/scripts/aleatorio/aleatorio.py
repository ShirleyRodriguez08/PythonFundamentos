import random


LISTA_NUMEROS = [*range(101)]


def num_aletorio(a, b, cantidad):
    """
    Funcion que permite obtener una cantidad determinada de numeros aleatorios en un rango
    """
    list_num = []
    for i in range(cantidad):
        list_num.append(random.randint(a,b)) # random.choise(LISTA_NUMEROS)
    return list_num 

def mostrar_lista(lista):
    print(lista)

def sort_list(lista):
    print(sorted(lista))

if __name__ == '__main__':
    
    x =num_aletorio(0,100, 20)

    mostrar_lista(x)

    sort_list(x.copy())




