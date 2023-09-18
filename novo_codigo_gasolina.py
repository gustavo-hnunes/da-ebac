import seaborn as sns
import pandas as pd
import csv

#Carregando infos
gas = pd.read_csv('gasolina.csv')

#Construindo e apresentando o gráfico
grafico = sns.lineplot(data=gas, x='dia', y='venda', color='Green')
grafico.set(title='Preços médio da gasolina no primeiros dias do mês de 07/2021 em SP Capital', xlabel='Dias', ylabel='Preço Médio')

#Salvando o gráfico
grafico.get_figure().savefig('/content/da-ebac/preco_medio_gasolina.png')