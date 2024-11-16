
# Relatório: Descrição do Conjunto de Dados

### 1. Introdução
Este relatório descreve as características principais do conjunto de dados utilizado para avaliar a influência de fatores socioeconômicos na expectativa de vida. O objetivo é fornecer uma visão geral do conteúdo, qualidade e estrutura dos dados, preparando-os para análise posterior.

### 2. Fonte dos Dados

- Origem: Dados provenientes do banco público internacional: [Global Country Information Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023)
- Período Abrangido: Dados coletados de **01/01/2023** a **31/12/2023**.
- Nível de Agregação: Indicadores por país.

### 3. Estrutura do Conjunto de Dados

O conjunto de dados contém 196 registros e 13 variáveis, conforme descrito abaixo:

|Variável|Tipo|Descrição|Unidade|
|---------------|---------------|---------------|---------------|
|Density(P/Km2)| |Densidade populacional por quilômetro quadrado|Pessoas/km²|
|Birth Rate| Numérica |Taxa de nascimentos por 1.000 habitantes|Nascimentos por 1.000 hab.|
|Fertility Rate	|Numérica|Número médio de filhos por mulher|Filhos/mulher|
|Infant mortality	|Numérica|Taxa de mortalidade infantil (crianças < 1 ano)|Mortes por 1.000 nascidos|
|Life expectancy	|Numérica|Expectativa média de vida ao nascer|Anos|
|Physicians per thousand	|Numérica|Número de médicos por mil habitantes|Médicos/mil habitantes|
|Co2-Emissions	|Numérica|Emissões de CO2 per capita|Toneladas|
|CPI|Numérica|Índice de Preços ao Consumidor|Escala|
|CPI Change (%)	|Numérica|Mudança percentual no CPI de um ano para outro|Percentual (%)|
|Out of pocket health expenditure	|Numérica|Percentual de gastos com saúde pagos diretamente pelo indivíduo|Percentual (%)|
|Population: Labor force participation (%)	|Numérica|Taxa de participação da força de trabalho na população|Percentual (%)|
|GDP	|Numérica|Produto Interno Bruto per capita|USD|
|Unemployment rate	|Numérica|Taxa de desemprego|Percentual (%)|


### 4. Qualidade dos Dados

- **Valores Ausentes:**
  - 0% de valores ausentes detectados
  - **Tratamento sugerido:** Calculo de média e mediana
- **Outliers:**
  - Foram detectados **148 outliers** em 13. Um exemplo é GDP com 21 outliers.
  - **Tratamento sugerido:** excluir os outliers com base no impacto na análise.
