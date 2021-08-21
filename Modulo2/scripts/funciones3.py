

def sumar(num1, num2):
    return num1 + num2

def media_aritmetica(cantidad_numeros):
    lista_numeros = []
    for i in range(cantidad_numeros):
        numero = int(input(f'Ingrese el {i+1} numero: '))
        lista_numeros.append(numero)
    
    sumatoria = 0
    for e in lista_numeros:
        sumatoria += e
        
    return sumatoria / cantidad_numeros

def imprimir_triangulo(altura):
    for i in range(altura):
        print('#' * (i+1))

print("Bienvenido al menú interactivo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) Sumar dos números
    2) Realiza la media aritmética de un conjunto de numeros
    3) Mostrar un triangulo segun una altura
    4) Salir""")
    
    opcion = input()
    if opcion == '1':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        suma = sumar(n1,n2)
        print(f"El resultado de la suma es: {suma}")
    
    elif opcion == '2':
        cantidad = int(input("Ingrese la cantidad de numeros a introducir: "))
        media = media_aritmetica(cantidad)
        print('La media aritmetica es: {}'.format(media))
            
    elif opcion =='3':
        altura = int(input("Ingrese la altura del triangulo: "))
        imprimir_triangulo(altura)
    
    elif opcion =='4':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")