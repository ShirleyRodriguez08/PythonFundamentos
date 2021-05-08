

def saludar():
    print("Hola, espero que te lo estés pasando bien")

def sumar_dos_numeros(a, b):
    return a + b

def triangulo_invertido(h):

    for i in range(1, h + 1 ):
        print(" " * (h-i) + "#" * i)



print("Bienvenido al menú interactivo")
bandera = True
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Generar Triangulo 
    4) Salir""")
    
    opcion = input()
    if opcion == '1':
        saludar()
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))

        suma = sumar_dos_numeros(n1,n2)
        print(f"El resultado de la suma es: {suma}")
    elif opcion =='3':
        h = int(input('Ingrese la altura del triangulo: '))
        triangulo_invertido(h)
        
    elif opcion =='4':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        #bandera = False
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
