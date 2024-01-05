import pandas as pd
from datetime import datetime

def Main_lib():
    # Iniciando a leitura da planilha em excel
    df=pd.read_excel('Planilha_Exemplo.xlsx')
    # Criando variáveis que tem o mesmo dado do nome da coluna da planilha
    nome_da_coluna_vencimento='DATA DE VENCIMENTO'
    nome_da_coluna_pagamento='PAGAMENTO'
    # Data de hoje
    hoje=datetime.now()
    # Criando colunas novas na planilha
    df['Data_Valida']=df[nome_da_coluna_vencimento].apply(lambda x: True if pd.to_datetime(x)>=hoje else False)
    df['Mensagem_Necessária']=df.apply(lambda row: True if row[nome_da_coluna_pagamento]=='Não' and row['Data_Valida']==False else False, axis=1)
    return df