print("Bienvenido al menú interactivo")
bandera = True

while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    
    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
        break
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print(f"El resultado de la suma es: {n1+n2}")
        break
    elif opcion =='3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        #bandera = False
        break # Finalizar el bucle
    else:
        print("Comando desconocido, vuelve a intentarlo")
    
    print('Retornando a while')

print('Saliste del Programa!')
