


semaforo = input('Ingrese el estado del semaforo: ')
semaforo = semaforo.lower()


if semaforo == 'verde':
    print('puede cruzar la calle')
elif semaforo in ['amarillo', 'rojo']:
    print('no puede cruzar la calle')
else:
    print('no es un valor admitido del semaforo')

