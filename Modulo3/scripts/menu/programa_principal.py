
import validacion_datos as vali
import triangulo as t

from funciones_avanzadas import factorial, luhn

OPCIONES = """¿Qué quieres hacer? Escribe una opción
    1) Sumar dos números
    2) Mostrar Triangulo
    3) Calcular Factorial
    4) Validar Tarjeta
    5) Salir"""

def sumar(a,b):
    return a +b

if __name__ == '__main__':
    print("Bienvenido al menú interactivo")
    while True:
        print(OPCIONES)
        respuesta = input()
        if respuesta == '1':
            n1 = vali.solicitar_entero('Introduce el primer numero: ')
            n2 = vali.solicitar_entero('Introduce el segundo numero: ')
            
            print(f"El resultado de la suma es: {sumar(n1,n2)}")
        elif respuesta == '2':
            altura = vali.solicitar_entero('Introduce la altura: ')
            t.mostrar_triangulo(altura)
        elif respuesta =='3':
            
            numero = vali.solicitar_entero('Ingrese el numero a calcular su factorial: ')
            f = factorial.factorial_recursivo(numero)
            print(f'el factorial de x = {numero} es {f}')
        elif respuesta =='4':
            tarjeta_valida = luhn.algoritmo_luhn(input('Ingrese una tarjeta'))
            print(f'La tarjeta es {tarjeta_valida}')
        elif respuesta =='5':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")