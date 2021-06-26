# librerias nativas
import os

# liberias externas
import pandas as pd

# librerias propias


if __name__ == '__main__':
    
    dicx= {
        "nombre": ["Rick", "Morty"],
        "apellido": ["Sanchez", "Smith"],
        "edad": [60, 14]
    }
    df_rick_morty = pd.DataFrame(dicx)
    
    print(df_rick_morty)
