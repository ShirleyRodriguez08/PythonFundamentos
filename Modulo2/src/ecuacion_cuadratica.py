# 1.importamos las liberias necesarias
from math import sqrt



# 2. constantes


# 3. funciones

def introduce_numero():
    coeficientes = [] 
    for i in range(3):
        x = int(input(f'Ingrese el valor de x{i}: '))
        coeficientes.append(x)

    return coeficientes

def calcular_raices(a, b, c):
    if a != 0:
        # calculo discriminante
        d= (b**2 - 4*a*c)
    
        if d<0: 
            print('Ecuación no presenta solución real')
        else: 
            x1= (-b+ sqrt(d))/(2*a)
            x2= (-b- sqrt(d))/(2*a)
            print(f'Los valores son {x1} y {x2}')
    else:     
        print('El valor de a debe ser distinto a cero')

# 4. programa principal


#a = introduce_numero()
#  calculo de las raices de la ecuacion
print('calculando ecuacion 1')
calcular_raices(2, 4, -6)
print('calculando ecuacion 2')
calcular_raices(1, 2, 1)
print('calculando ecuacion 3')
calcular_raices(3, 4, 5)