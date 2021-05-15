# 1. Importando librerias
# librerias de python
import sys
import pandas as pd # pd -> alias de liberias

# librerias propias
from operaciones import opermath as mathx 
from funciones_especiales import triangulo

import validaciones as v

# 2. constantes

# 3. funciones

# 4. Mi programa
if __name__=='__main__':
    print("Bienvenido al menú interactivo")

    while True:
        print("""¿Qué quieres hacer? Escribe una opción
        1) Sumar dos números
        2) Mostrar triangulo
        3) Salir""")

        opcion = input()
        if opcion == '1':
            n1 = v.ingresa_numero("Introduce el primer número: ")
            n2 = v.ingresa_numero("Introduce el primer número: ")

            suma = mathx.sumar(n1,n2)
            print(f"El resultado de la suma es: {suma}")
        elif opcion == '2':
            n = v.ingresa_numero_entero('introduce la altura del triangulo: ')
            triangulo.mostrar_triangulo(n)
        elif opcion =='3':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            #bandera = False
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")