# 1. librerias
# librerias de python
import math
import sys

# librerias propias
import ingreso_datos as ing
from triangulos import triangulo as t
import mate.factorial as f


# 2. constantes
PI = 3.14

# 3. Funciones y/ o clases

def main():
    print("Bienvenido al menú interactivo")
    
    while True:
        print("""¿Qué quieres hacer? Escribe una opción
        1) Saludar
        2) Calcular factorial de un numero
        3) Mostrar un triangulo
        4) Salir""")
        
        opcion = input() # me devuelve un string ''
        if opcion == '1':
            print("Hola, espero que te lo estés pasando bien")
        elif opcion == '2':
            num = ing.ingreso_entero('Ingrese el numero a calcular: ')
            fac = f.factorial(num)
            print(f"El factorial es: {fac}")

        elif opcion =='3':
            h = ing.ingreso_entero('Ingrese la altura del triangulo: ')
            triangulo.mostrar_triangulo(h)

        elif opcion =='4':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")


#  4. Mi programa
if __name__ == '__main__':
    # llamando programa
    main()

    