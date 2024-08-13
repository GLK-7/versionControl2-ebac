
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  # Import necessário para exibir e salvar o gráfico

# Ler o arquivo CSV e passar para um DataFrame
df_gasolina = pd.read_csv('gasolina.csv')
df_gasolina.head() 

# Gerar gráfico de linha
chart = sns.lineplot(data=df_gasolina, x='dia', y='venda')
chart.set_title('Preço da Gasolina por Dia')
chart.set_xlabel('Dia')
chart.set_ylabel('Preço')  

# Salvar o gráfico como PNG
plt.savefig('gasolina.png', format='png')

print("Arquivo gasolina.png criado com sucesso.")
