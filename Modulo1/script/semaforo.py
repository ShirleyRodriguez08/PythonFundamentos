

semaforo = input("Ingrese el color del semaforo: ")
semaforo = semaforo.lower()

if semaforo == "verde":
    print("cruce la calle")
elif semaforo == "amarrillo" or semaforo == "rojo":
    print("no cruce")
else:
    print("no es un estado de semaforo definido")
