import os

ESCRIBIR = 'Hola, se esta escribiendo una linea de código'

with open('text.txt', mode='w',encoding='utf-8') as p:
    p.write(ESCRIBIR)
