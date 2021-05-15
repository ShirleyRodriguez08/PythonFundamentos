import math


def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def potenciacion(numero, n=2):
    return math.pow(numero,n)


if __name__=='__main__':

    print(potenciacion(2))