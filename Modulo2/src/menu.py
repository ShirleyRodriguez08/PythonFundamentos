


n1 = float(input("Digite primer número: "))
n2 = float(input("Digite segundo número: "))


while(True):
    print("****MENU****")
    print("1.- Sumar dos números")
    print("2.- Restar dos números")
    print("3.- Multiplicar dos números")
    print("4.- Salir del programa")
    
    opcion = input("Opción: ")
    if opcion == '1':
        resultado = n1 + n2
    elif opcion == '2':
        resultado = n1-n2
    elif opcion == '3':
        resultado =n1*n2
    elif opcion =='4':
        break
    else:
        print("Digite una opción válida")
        continue
     
    print("El resultado es:",resultado)
