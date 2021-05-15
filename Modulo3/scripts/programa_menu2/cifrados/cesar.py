# 1. Librerias
import sys

#2. Constantes
ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 3. Funciones
def cifrado_cesar(plaintext:str)->str:
    return NotImplementedError

# 4. Programa Principal
if __name__=='__main__':

    plaintext= "hello, world"

    k = int(input("Valor de desplazamiento: "))

    ciphertext = ""
    for l in plaintext:
        
        if l.upper() in ABECEDARIO:
            ciphertext += l # cifrado cesar 
        else:
            ciphertext += l
    
    print(f'El texto cifrado es : {ciphertext}')

    pass

# for c in texto:
#     if c in abc:
#         cifrado += abc[(abc.index(c)+k%(len(abc)))]
#     else:
#         cifrado+=c 
# print("texto cifrado: ",cifrado)
