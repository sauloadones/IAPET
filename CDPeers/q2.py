import pandas as pd

arquivo_excel = 'cdpeers.xlsx'


cadastroEstoque = pd.read_excel(arquivo_excel, sheet_name='Cadastro de Estoque', skiprows=1)
cadastroProdutos = pd.read_excel(arquivo_excel, sheet_name='Cadastro Produtos', skiprows=1)
transacoesVendas = pd.read_excel(arquivo_excel, sheet_name='Transações Vendas', skiprows=1)


cadastroEstoque.columns = cadastroEstoque.columns.str.strip().str.upper()
cadastroProdutos.columns = cadastroProdutos.columns.str.strip().str.upper()
transacoesVendas.columns = transacoesVendas.columns.str.strip().str.upper()


transacoesVendas.rename(columns={'ID PRODUTO': 'ID_PRODUTO', 'VALOR ITEM': 'VALOR_ITEM'}, inplace=True)
cadastroProdutos.rename(columns={'ID PRODUTO': 'ID_PRODUTO'}, inplace=True)

cadastroEstoque['VALOR_UNITARIO'] = cadastroEstoque['VALOR ESTOQUE'] / cadastroEstoque['QTD ESTOQUE']


produtos_estoque = cadastroProdutos.merge(
    cadastroEstoque[['ID ESTOQUE', 'VALOR_UNITARIO']],
    on='ID ESTOQUE',
    how='left'
)


vendas_completo = transacoesVendas.merge(produtos_estoque[['ID_PRODUTO', 'VALOR_UNITARIO']], on='ID_PRODUTO', how='left')


vendas_completo['MARGEM_LUCRO'] = vendas_completo['VALOR_ITEM'] - vendas_completo['VALOR_UNITARIO']


margem_por_produto = vendas_completo.groupby('ID_PRODUTO')[['VALOR_ITEM', 'VALOR_UNITARIO', 'MARGEM_LUCRO']].mean().reset_index()

print("\n Margem de lucro média por produto:")
print(margem_por_produto)
