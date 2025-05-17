import pandas as pd

   

arquivo_excel = 'cdpeers.xlsx'

transacoes = pd.read_excel(arquivo_excel, sheet_name='Transações Vendas', skiprows=1)

transacoes.columns = transacoes.columns.str.strip().str.upper()

transacoes['DATA NOTA'] = pd.to_datetime(transacoes['DATA NOTA'])
transacoes['MES'] = transacoes['DATA NOTA'].dt.to_period('M')

ranking_produtos_valor = transacoes.groupby(['MES', 'ID PRODUTO'])['VALOR ITEM'].sum().reset_index()
ranking_produtos_valor = ranking_produtos_valor.sort_values(by=['MES', 'VALOR ITEM'], ascending=[True, False])

print(ranking_produtos_valor)
