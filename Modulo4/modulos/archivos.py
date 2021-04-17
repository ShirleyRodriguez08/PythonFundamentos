# %%
import os 

# por defecto el modo es r
with open('./src/texto.txt') as f:

    data = f.readlines()

    print(type(f))

print(data)
# %%

print('imprimiendo la primera linea')
data[-2]
# %%
