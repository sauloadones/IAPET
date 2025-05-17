
import pandas as pd



arquivo_excel = 'cdpeers.xlsx'

transacoes = pd.read_excel(arquivo_excel, sheet_name='Transações Vendas', skiprows=1)

transacoes.columns = transacoes.columns.str.strip().str.upper()

transacoes['DATA NOTA'] = pd.to_datetime(transacoes['DATA NOTA'])
transacoes['MES'] = transacoes['DATA NOTA'].dt.to_period('M')

ranking_produtos_qtd = transacoes.groupby(['MES', 'ID PRODUTO'])['QTD ITEM'].sum().reset_index()
ranking_produtos_qtd = ranking_produtos_qtd.sort_values(by=['MES', 'QTD ITEM'], ascending=[True, False])

print(ranking_produtos_qtd)
