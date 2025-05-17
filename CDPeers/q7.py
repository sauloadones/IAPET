import pandas as pd

arquivo_excel = 'cdpeers.xlsx'

transacoes = pd.read_excel(arquivo_excel, sheet_name='Transações Vendas', skiprows=1)
produtos = pd.read_excel(arquivo_excel, sheet_name='Cadastro Produtos', skiprows=1)

transacoes.columns = transacoes.columns.str.strip().str.upper()
produtos.columns = produtos.columns.str.strip().str.upper()

transacoes['DATA NOTA'] = pd.to_datetime(transacoes['DATA NOTA'])
transacoes['MES'] = transacoes['DATA NOTA'].dt.to_period('M')

df = transacoes.merge(produtos[['ID PRODUTO', 'CATEGORIA']], on='ID PRODUTO', how='left')

media_valor_categoria = df.groupby(['MES', 'CATEGORIA'])['VALOR ITEM'].mean().reset_index()

print(media_valor_categoria)