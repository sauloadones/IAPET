import pandas as pd

arquivo_excel = 'cdpeers.xlsx'

cadastro_estoque = pd.read_excel(arquivo_excel, sheet_name='Cadastro de Estoque', skiprows=1)
cadastro_fornecedores = pd.read_excel(arquivo_excel, sheet_name='Cadastro Fornecedores', skiprows=1)

cadastro_estoque.columns = cadastro_estoque.columns.str.strip().str.upper()
cadastro_fornecedores.columns = cadastro_fornecedores.columns.str.strip().str.upper()

cadastro_estoque['DATA ESTOQUE'] = pd.to_datetime(cadastro_estoque['DATA ESTOQUE'])
cadastro_estoque['MES'] = cadastro_estoque['DATA ESTOQUE'].dt.to_period('M')

estoque_mensal = cadastro_estoque.groupby(['MES', 'ID FORNECEDOR'])['QTD ESTOQUE'].sum().reset_index()

estoque_mensal = estoque_mensal.merge(
    cadastro_fornecedores[['ID FORNECEDOR', 'NOME FORNECEDOR']],
    on='ID FORNECEDOR',
    how='left'
)

ranking_fornecedores = estoque_mensal.sort_values(by=['MES', 'QTD ESTOQUE'], ascending=[True, False])

print(ranking_fornecedores)
