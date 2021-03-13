
# importar librerias

import os
import math


import validacion as v # 'v' es un alias para la libreria


# funcion que valida ingreso de numero


#  solictamos ingreso de capital a depositar

capital = v.val_num_float("Ingrese Cantidad a depositar")

# calculamos

i = 0.04

for t in range(1,4):
    a1 = capital * ((1+ i)**t)
    print(f"La cantidad del {t} año es: {a1:.2f}")



