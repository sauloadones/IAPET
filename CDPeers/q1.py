import pandas as pd

arquivo_excel = 'cdpeers.xlsx'


cadastro_produtos = pd.read_excel(arquivo_excel, sheet_name='Cadastro Produtos', skiprows=1)


transacoes_vendas = pd.read_excel(arquivo_excel, sheet_name='Transações Vendas', skiprows=1)



transacoes_vendas.columns = transacoes_vendas.columns.str.strip().str.upper()
cadastro_produtos.columns = cadastro_produtos.columns.str.strip().str.upper()
print(cadastro_produtos.columns.tolist())
transacoes_vendas.rename(columns={
    'ID PRODUTO': 'ID_PRODUTO', 
    'VALOR ITEM': 'VALOR_ITEM'}, 
    inplace=True)
cadastro_produtos.rename(columns={'ID PRODUTO': 'ID_PRODUTO'}, inplace=True )


df = transacoes_vendas.merge(cadastro_produtos[['ID_PRODUTO', 'CATEGORIA']], on='ID_PRODUTO', how='left')

total_por_categoria = df.groupby('CATEGORIA')['VALOR_ITEM'].sum().reset_index()



print("Valor total de vendas por categoria:")
print(total_por_categoria)