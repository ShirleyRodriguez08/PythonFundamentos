import math

import validacion # llamo a la libreria que contiene mis funciones

# de la carpeta 'check' importo el archivo 'valida'
from check import valida


def discriminante(a,b,c):
    return math.pow(b,2) - 4 * a * c


# solicito valores
a = valida.val_num_int('Ingrese el coeficiente a')
b = valida.val_num_int('Ingrese el coeficiente b')
c = valida.val_num_int('Ingrese el coeficiente c')


#  calculo las raices de la ecuacion
if a != 0:    
    d = discriminante(a,b,c)
    
    if d >= 0:
        x1 = (-b + math.sqrt(d) ) / 2
        x2 = (-b - math.sqrt(d) ) / 2
        print(f'Soluciones x1: {x1}, x2: {x2}')
    else:
        print('No presenta soluciones reales')
else:
    print('no es una ecuación de 2do grado')