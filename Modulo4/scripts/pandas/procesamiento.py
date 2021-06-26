import os
import time

import pandas as pd



path_file = r'C:\Users\gon_2\OneDrive - UNIVERSIDAD NACIONAL DE INGENIERIA\Desktop\PythonFundamentos\Modulo4\data\primary_results.csv'

# 1. leo data
inicio = time.time()

df = pd.read_csv(path_file,sep=',',encoding='utf-8')

states_list = df.state.unique()

# 2. proceso y guardo info

for state in states_list:
    
    df_var = df[df['state'] == state]

    df_var.to_excel(f'./out/data_{state}.xlsx',sheet_name=state,index=False)

print('Procesamiento finalizado en {} s'.format( time.time() - inicio))

