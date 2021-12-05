import pandas as pd
import os


INPUT_PATH = './data_partidos.xlsx'
OUTPU_PATH = './info_estados/{}.xlsx'


if __name__ == "__main__":
    
    df = pd.read_excel(INPUT_PATH,sheet_name='dataProcesadaPartidos')
    
    if not os.path.isdir('./info_estados'):
        os.mkdir('./info_estados')

    estados = df.state.unique()
    for estado in estados:
        # filtrando información segun el estado
        condition = (df.state == estado)
        df2 = df[condition]
        #print(estado)
        path_final = OUTPU_PATH.format(estado)
        df2.to_excel(path_final, sheet_name=estado, encoding='utf-8', index=False)
    
    

