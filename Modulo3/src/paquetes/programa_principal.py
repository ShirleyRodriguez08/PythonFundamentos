# 1. Importamos librerias
import sys
import math

from ingreso_datos import  ingrese_numero, ingrese_numero_float
from operaciones.operaciones_basicas import sumar, potencia
from operaciones.media import media_aritmetica
from triangulos.triangulos import imprimir_triangulo

#import ingreso_datos 


# 2. Constantes

# 3. Funciones
def saludar():
    print('hola a todos')

# 4. Mi programa
if __name__=="__main__":
    print("Bienvenido al menú interactivo")
    while True:
        print("""¿Qué quieres hacer? Escribe una opción
        0) saludar
        1) Sumar dos números
        2) Realiza la media aritmética de un conjunto de numeros
        3) Mostrar un triangulo segun una altura
        4) Salir""")
    
        opcion = input()
        if opcion == '0':
            saludar()
        elif opcion == '1':
            n1 = ingrese_numero_float("Introduce el primer número: ")
            n2 = ingrese_numero_float("Introduce el segundo número: ")
            suma = sumar(n1,n2)
            print(f"El resultado de la suma es: {suma}")
        
        elif opcion == '2':
            cantidad = ingrese_numero("Ingrese la cantidad de numeros a introducir: ")
            media = media_aritmetica(cantidad)
            print('La media aritmetica es: {}'.format(media))
        
        elif opcion =='3':
            altura = ingrese_numero("Ingrese la altura del triangulo: ")
            imprimir_triangulo(altura)
        elif opcion =='4':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")