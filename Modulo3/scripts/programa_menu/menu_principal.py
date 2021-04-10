# Librerias
import os

# librerias propias
from operaciones import operacion 
from operaciones_avanzadas import factorial
from validaciones import valida as v

# constantes
TIPO_CAMBIO = 3.65

# funciones y/o clases
def saludar():
    print('Hola a todos')

# Programa principal
if __name__ == "__main__":
    print("Bienvenido al menú interactivo")
    
    while True:
        print(""¿Qué quieres hacer? Escribe una opción
        1) Saludar
        2) Sumar dos números
        3) Calcular factorial de un número
        4) Salir""")

        opcion = input()
        if opcion == '1':
            saludar()
        elif opcion == '2':
            n1 = v.valida_float(' Introduce el primero número: ')
            n2 = v.valida_float(' Introduce el segundo número: ')

            suma = operacion.sumar(n1, n2)
            print(f"El resultado de la suma es {suma}")

        elif opcion =='3':
            num = v.valida_numero('Introduce el número del factorial: ')

            print(f'El factorial es {factorial.factorial_num(num)}') 
            
        elif opcion =='4':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")