import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

df = pd.read_csv('Dadoslimpos.csv', sep=';')

# Convertendo colunas com vírgula como separador decimal para float
columns_to_convert = [
    'Density(P/Km2)', 'Birth Rate', 'Fertility Rate', 'Infant mortality', 
    'Life expectancy', 'Physicians per thousand', 'Co2-Emissions', 'CPI', 
    'CPI Change (%)', 'Out of pocket health expenditure', 
    'Population: Labor force participation (%)', 'GDP', 'Unemployment rate'
]

# Limpando as colunas substituindo vírgulas e convertendo para float
for col in columns_to_convert:
    if col in ['CPI Change (%)', 'Out of pocket health expenditure', 'Population: Labor force participation (%)', 'Unemployment rate']:
        df[col] = df[col].str.replace(',', '.').str.replace('%', '').astype(float) / 100
    else:
        df[col] = df[col].str.replace(',', '.').astype(float)

# Tirando a ultima coluna
df = df.drop(df.columns[-1], axis=1)

# Reordenando colunas para ter 'Expectativa de vida' como a última coluna
cols = [col for col in df.columns if col != 'Life expectancy'] + ['Life expectancy']
df = df[cols]

x_dados = df.iloc[:, 0:14].values  # Atributos
y_dados = df.iloc[:, 14].values    # Classe

# Escalonamento
scaler = StandardScaler()
x_dados = scaler.fit_transform(x_dados)

# Dividindo dados em conjuntos de treinamento e teste
x_dados_treinamento, x_dados_teste, y_dados_treinamento, y_dados_teste = train_test_split(
    x_dados, y_dados, test_size=0.15, random_state=0
)

regressor_multiplo = LinearRegression()
regressor_multiplo.fit(x_dados_treinamento, y_dados_treinamento)

# Exibindo coeficientes do modelo e pontuações R-quadrado
print("Coeficiente do modelo:", regressor_multiplo.coef_)
print("R² treinamento:", regressor_multiplo.score(x_dados_treinamento, y_dados_treinamento))
print("R² teste:", regressor_multiplo.score(x_dados_teste, y_dados_teste))

previsoes = regressor_multiplo.predict(x_dados_teste)
print("Previsões:", previsoes)

# Calculando e exibindo o erro absoluto médio
mae = mean_absolute_error(y_dados_teste, previsoes)
print("Erro Absoluto Médio:", mae)

plt.scatter(y_dados_teste, previsoes)
plt.plot([y_dados_teste.min(), y_dados_teste.max()], [y_dados_teste.min(), y_dados_teste.max()], color='red', linestyle='--')
plt.xlabel('Valores reais')
plt.ylabel('Previsões')
plt.title('Comparação entre valores reais e previsões')
plt.show()

selected_vars = ['Density(P/Km2)', 'Infant mortality', 'Birth Rate']
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

for i, var in enumerate(selected_vars):
    ax = axes[i]
    ax.scatter(df[var], df['Life expectancy'], alpha=0.5)
    ax.set_xlabel(var)
    ax.set_ylabel('Expectativa de vida')
    ax.set_title(f'Relação entre {var} e Expectativa de vida')

# Ajusta o layout para evitar sobreposição
plt.tight_layout()
plt.show()

