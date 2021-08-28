
# Con funcion recursiva
def divide_num():
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
        return divide_num()



# Solicitar un numero de manera forzosa
# while True:
#     try:
#         nota = int(input("Ingrese su nota: "))
#         print(f'La nota ingresada es {nota}')
#         break # salimos del bucle
#     except:
#         print("Ingrese bien el numero, vuelva a intentar")


# llamada funcion
divide_num()




