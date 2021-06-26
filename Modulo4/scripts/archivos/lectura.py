import os

path_file = './data.txt'

# lectura
with open(path_file, mode='r') as f:
    # recupero la data del archivo
    data = f.read()
    print(data)



