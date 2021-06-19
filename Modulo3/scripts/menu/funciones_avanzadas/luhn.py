
def algoritmo_luhn(tarjeta :str):
    # paso1
    tarjeta_invertida =  tarjeta[::-1]
    lista_impares = []
    lista_pares = []
    for i, n in enumerate(tarjeta_invertida):
        if i % 2==1:
            lista_impares.append(int(n) * 2)
            continue
        lista_pares.append(int(n))
    
    # paso2:
    suma_d = 0
    for e in lista_impares:
        if e // 10 == 0:
            suma_d += e
        else:
            suma_d += e // 10
            suma_d += e % 10
    suma_d += sum(lista_pares)
    # Paso3 : Validar que último digito de suma sea '0'
    if suma_d % 10==0:
        return True
    else:
        return False

