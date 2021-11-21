# librerias python
import datetime

# librerias propias
import operaciones
import triangulos as t # alias de importacion
import funciones_especiales as especial_func
import clases

def ingrese_entero(msg : str = "Ingrese un numero: ") -> int :
    """Retorna un numero entero ingresado por teclado
    """
    try:
        n =  int(input(msg))
        return n
    except:
        print("Ingrese bien el numero")
        return ingrese_entero(msg)

def ingrese_float(msg : str = "Ingrese un numero: ") -> float :
    """Retorna un numero float ingresado por teclado
    """
    try:
        n =  float(input(msg))
        return n
    except:
        print("Ingrese bien el numero")
        return ingrese_entero(msg)


if __name__ == "__main__":
    print("Bienvenido al menú interactivo")
    while True:
        print("""¿Qué quieres hacer? Escribe una opción
        1) Sumar dos números
        2) Factorial de un números
        3) Mostrar triangulo
        4) Clase Restaurante
        5) Salir""")

        opcion = input()
        if opcion == '1':
            a  =  ingrese_float("Introduce un numero: ")
            b  =  ingrese_float("Introduce un numero: ")

            resultado = operaciones.sumar(a, b)

            print(f"La suma de los numeros es {resultado}")
        elif opcion == '2':
            n  =  ingrese_entero("Introduce un numero: ")
            factorial = especial_func.funcion_factorial(n)
            print(f"El factorial es: {factorial}")
        elif opcion =='3':
            h  =  int(input("Introduce un numero: "))
            t.mostrar_triangulo(h)

        elif opcion =='4':
            nombre = input("Ingrese el nombre del restaurante: ")
            cusine = input("Ingrese el tipo de comida del restaurante: ")
            restaurante1 = clases.Restaurant(nombre, cusine)
            restaurante1.describe_restaurant()

        elif opcion =='5':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")