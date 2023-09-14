import seaborn as sns
import pandas as pd
import csv

#Carregando infos
gas = pd.read_csv('gasolina.csv')

#Construindo e apresentando o gráfico
grafico = sns.lineplot(data=gas, x='dia', y='venda', color='Red')
grafico.set(title='Preços médio da gasolina no primeiros dias de Julho/2021 em São Paulo', xlabel='Dias do mês', ylabel='Preço Médio da Gasolina')

#Salvando o gráfico
grafico.get_figure().savefig('/content/da-ebac/preco_medio_gasolina.png')