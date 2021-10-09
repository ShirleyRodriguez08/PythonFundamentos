import aleatorio


if __name__ == '__main__':
    # generando lista de numeros aleatorios
    lista_random = aleatorio.num_aletorio(0,100, 20)

    # mostrando lista
    aleatorio.mostrar_lista(lista_random)

    # mostrando lista ordenanda
    aleatorio.sort_list(lista_random.copy())