#Dicionario de Dados

# ABR   : Abrangência geográfica (ex.: Brasil)
# DEP   : Tipo de rede administrativa (Federal, Estadual, Municipal)
# ESC   : Escolaridade dos docentes (Superior, Sem Superior, Total)
# ND    : Número de docentes declarados no Censo Escolar
# MD    : Remuneração bruta média (R$)
# R40h  : Remuneração padronizada estimada para jornada de 40 horas semanais (R$)
# CH    : Carga horária média semanal (horas/semana)
# DP    : Desvio padrão da remuneração entre os docentes (R$)

# Observações:
# - As colunas 'DEP' e 'ESC' foram usadas como grupos de análise.
# - As colunas 'MD' e 'R40h' foram utilizadas para cálculo e visualização da remuneração.
# - A coluna 'CH' foi usada na análise de mediana da remuneração por carga horária




import pandas as pd
import matplotlib.pyplot as plt

arquivo = './Remuneracao_docentes_Brasil_2020.xlsx'
df = pd.read_excel(arquivo, sheet_name=0)

df.columns = [
    'ano', 'abrangencia', 'dependencia', 'escolaridade', 'n_docentes',
    'porcentagem_localizados', 'quartil_1', 'mediana', 'media',
    'quartil_3', 'desvio_padrao', 'carga_horaria', 'remuneracao_40h'
]

df = df[pd.to_numeric(df['ano'], errors='coerce').notnull()] ## Remove as linhas sem ano valido


colunas_numericas = [
    'n_docentes', 'porcentagem_localizados', 'quartil_1', 'mediana',
    'media', 'quartil_3', 'desvio_padrao', 'carga_horaria', 'remuneracao_40h'
]


df[colunas_numericas] = df[colunas_numericas].apply(pd.to_numeric, errors='coerce')

df_renomeado = df.rename(columns={
    'abrangencia': 'ABR',
    'dependencia': 'DEP',
    'escolaridade': 'ESC',
    'n_docentes': 'ND',
    'media': 'MD',
    'remuneracao_40h': 'R40h',
    'carga_horaria': 'CH',
    'desvio_padrao': 'DP'
})



print("\n Estrutura do DataFrame:")
print(df_renomeado.info())


print("\n Estatisticas descritivas:")
print(df_renomeado[['MD', 'R40h', 'CH', 'DP']].describe())




media_dependencia = df_renomeado.groupby('DEP')['R40h'].mean().sort_values(ascending=False)
print("\nMédia de remuneração por tipo de rede (DEP):")
print(media_dependencia)


media_escolaridade = df_renomeado.groupby('ESC')['R40h'].mean().sort_values(ascending=False)
print("\nMédia de remuneração por escolaridade (ESC):")
print(media_escolaridade)


mediana_por_carga = df_renomeado.groupby('CH')['R40h'].median().sort_index()
print("\nMediana da remuneração (R40h) por carga horária média (CH):")
print(mediana_por_carga)



df_renomeado.groupby('DEP')['R40h'].mean().sort_values(ascending=False).plot(
    kind='bar', title='R40h Média por Tipo de Rede (DEP)', ylabel='R$', xlabel='Tipo de Rede', grid=True
)
plt.tight_layout()
plt.show()

df_renomeado.groupby('CH')['R40h'].median().sort_index().plot(
    kind='bar', title='Mediana da R40h por CH', ylabel='R$', xlabel='Carga Horária Média (h/sem)', grid=True
)
plt.tight_layout()
plt.show()



mediana_por_carga.plot(kind='line', marker='o', color='teal')
plt.title('Mediana da Remuneração (40h) por Carga Horária Média Semanal')
plt.xlabel('Carga Horária Média (horas/semana)')
plt.ylabel('Remuneração Mediana (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()


df_renomeado.to_csv('remuneracao_docentes_2020_abreviado.csv', index=False, encoding='utf-8')
