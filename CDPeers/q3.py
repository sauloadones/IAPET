import pandas as pd

arquivo_excel = 'cdpeers.xlsx'

transacoes = pd.read_excel(arquivo_excel, sheet_name='Transações Vendas', skiprows=1)
clientes = pd.read_excel(arquivo_excel, sheet_name='Cadastro Clientes', skiprows=1)

transacoes.columns = transacoes.columns.str.strip().str.upper()
clientes.columns = clientes.columns.str.strip().str.upper()

transacoes['DATA NOTA'] = pd.to_datetime(transacoes['DATA NOTA'])
transacoes['MES'] = transacoes['DATA NOTA'].dt.to_period('M')

ranking_clientes = transacoes.groupby(['MES', 'ID CLIENTE'])['QTD ITEM'].sum().reset_index()

ranking_clientes = ranking_clientes.merge(
    clientes[['ID CLIENTE', 'NOME CLIENTE']],
    on='ID CLIENTE',
    how='left'
)

ranking_clientes = ranking_clientes.sort_values(by=['MES', 'QTD ITEM'], ascending=[True, False])

print(ranking_clientes)
