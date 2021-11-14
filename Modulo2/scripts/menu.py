print("Bienvenido al menú interactivo")

bandera = True
while bandera:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Sumar de números
    2) Resta de números
    3) Multiplicacion de números
    4) Salir""")
    
    opcion = input()
    if opcion == '1':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la suma es: {n1+n2}")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la resta es: {n1-n2}")
    elif opcion =='3':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la multiplicacion es: {n1*n2}")
    elif opcion =='4':
        print("Gracias por usar la aplicacion")
        bandera = False
        #break
    else:
        print("Comando desconocido, vuelve a intentarlo")