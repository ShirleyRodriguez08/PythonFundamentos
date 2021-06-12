# %%
altura = int(input('Ingrese la altura del triangulo: '))
# %%
print(altura)
# %%
for i in range(1,altura+1):
    print('#'*i)
# %%
for i in range(1,altura+1):
    print(' ' * (altura-i) + '#' * i)
