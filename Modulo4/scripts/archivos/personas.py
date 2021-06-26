import os

RUTA = os.getcwd()


file_path = os.path.join(RUTA,'personas.txt')

with open(file_path, mode='r',encoding='utf-8') as f:
    data_personas = f.readlines()
    pass # end with

# print(data_personas)
lista_persona = []
for p in data_personas:
    # Separo linea por separador ';
    data_p = p.split(';')
    
    # almaceno data en diccionario
    dict_p = {
        'id': data_p[0],
        'nombre': data_p[1],
        'apellido': data_p[2],
        'fecha_nacimiento': data_p[3].strip()
    }
    lista_persona.append(dict_p)

print(lista_persona)