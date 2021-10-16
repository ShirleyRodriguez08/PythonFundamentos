import os
import pandas as pd





if __name__ == '__main__':
    
    df = pd.read_excel('./data_partidos.xlsx', sheet_name='data')


    if not os.path.isdir('./info_estados'):
        os.mkdir('./info_estados')

    estados = df.state.unique()
    for estado in estados:
        # filtrando información segun el estado
        condition = (df.state == estado)
        df2 = df[condition]

        # expotando data por estado
        df2.to_excel(f'./info_estados/{estado}.xlsx', sheet_name=estado, encoding='utf-8', index=False)
    
    
    os.system('pause')





