

def factoria(num):
    fac = 1
    for i in range(1, num+1):
        fac = fac * i
    return fac

def factorial_recursivo(num):
    if num == 1:
        return 1
    
    return num * factorial_recursivo(num-1)

x = 3

fact = factoria(x)
print(f'el factorial de x = {x} es {fact}')

print(f'el factorial de x = {x} es {factorial_recursivo(x)}')


