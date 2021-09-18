# creo archivo python con extención .py

estado_semaforo = input('Ingrese color del semaforo: ')

# 1. si es verde cruzo la calle
# 2. si es amarillo o rojo no cruzo
# 3. otra cosa -> no contemplado

if estado_semaforo == 'verde':
    print('Puedes cruzar la calle')
elif estado_semaforo == 'amarillo' or estado_semaforo=='rojo':
    print('no puedes cruzar la calle')
else:
    print('valor no contemplado')
