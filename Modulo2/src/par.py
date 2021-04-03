

def val_par(num):
    if num % 2 == 0:
        print(f'el número {num} es par')
    else:
        print(f'el número {num} es impar')
    
# 1. Ingresar un numero

list_num = [*range(100)]

for num in list_num:
    val_par(num)
