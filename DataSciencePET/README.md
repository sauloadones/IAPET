# 📊 Análise da Remuneração de Docentes da Educação Básica (INEP 2020)

Este projeto contém um dashboard interativo desenvolvido em Power BI para explorar a remuneração dos docentes da educação básica no Brasil com base nos dados públicos do INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira), referentes ao ano de 2020.

## 📁 Arquivo

- `remuneracao_docentes_2020.pbix` – Arquivo Power BI com todos os gráficos, tratamentos de dados e análises.

## 📌 Objetivos do Projeto

- Analisar a remuneração média padronizada (R40h) por:
  - Tipo de rede administrativa (Federal, Estadual, Municipal)
  - Escolaridade dos docentes
  - Faixas de carga horária média semanal
- Visualizar estatísticas como média, mediana e distribuição percentual.
- Preparar dados para visualizações em Power BI com qualidade para apresentação.

## 🧮 Fonte dos Dados

- Portal INEP — Indicadores Educacionais  
  🔗 [https://www.gov.br/inep](https://www.gov.br/inep)

## 📊 Visualizações incluídas

- Gráfico de barras da média da R40h por tipo de rede (`DEP`)
- Gráfico de barras da média da R40h por escolaridade (`ESC`)
- Gráfico de pizza da mediana da R40h por faixa de carga horária (`faixa_CH`)
- Tabelas de apoio com valores originais e classificados
- Rótulos, percentuais e painéis interativos

## ⚙️ Pré-processamento

Os dados foram tratados e limpos utilizando:

- Power Query (conversão de tipos, correção de escalas da coluna `CH`)
- Fórmulas DAX para criar a variável `faixa_CH`
- Normalização para permitir leitura correta de decimais no Power BI

## 🚀 Como usar

1. Clone o repositório ou baixe o arquivo `.pbix`
2. Abra no [Power BI Desktop](https://powerbi.microsoft.com/pt-br/desktop/)
3. Interaja com os filtros e gráficos
4. Adapte para novas bases, anos ou estados se desejar

---

© 2024 — Desenvolvido para fins educacionais e de análise pública.
