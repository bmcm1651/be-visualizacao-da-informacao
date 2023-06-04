import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ds = pd.read_csv(r'C:\Faculdade\trabalho Visualização da Informação\dataset_trabalho.csv')

#grafico 1 // genero%
data1 = ds['Gender'].value_counts()
plt.pie(data1, labels=data1.index, autopct='%1.1f%%')
plt.title('porcentagem de gênero')
plt.show()

#grafico 2 // trabalho - quantidade
data2= ds['Occupation'].value_counts()
profissões = data2.index
quantidade = data2.values
plt.bar(profissões, quantidade)
plt.xlabel('occupation')
plt.ylabel('count')
plt.show()

#grafico 3 // enfermeiras - quantidade p/ idade
age_blocks = ['21-30', '31-40', '41-50', '51-60']
enfermeiras = ds[ds['Occupation'] == 'Nurse']
plt.figure(figsize=(10, 6))
plt.fill_between(enfermeiras['Age'], enfermeiras.index)
plt.xlabel('Idade')
plt.ylabel('Número de enfermeiras')
plt.title('Distribuição da Idade das Enfermeiras')
plt.show()

#grafico 4 // correlação quantitativa entre idade e 'tempo de sono'/'qualidade do sono'/'nivel de estresse'
age_blocks = ['21-30', '31-40', '41-50', '50-60']
ds['Age Block'] = pd.cut(ds['Age'], bins=[20, 30, 40, 50, 150], labels=age_blocks)
enfermeiras = ds[ds['Occupation'] == 'Nurse']
correlations = ['Sleep Duration', 'Quality of Sleep', 'Stress Level']
correlation_data = {}
for correlation in correlations:
    correlation_data[correlation] = enfermeiras.groupby('Age Block')[correlation].mean()
bar_width = 0.2
age_blocks_indices = np.arange(len(age_blocks))
fig, ax = plt.subplots(figsize=(10, 6))
for i, correlation in enumerate(correlations):
    bar_positions = age_blocks_indices + (i * bar_width)
    ax.bar(bar_positions, correlation_data[correlation], width=bar_width, label=correlation)
ax.set_xlabel('Idade')
ax.set_ylabel('Quantidade')
ax.set_title('Análise - Enfermeiras')
ax.set_xticks(age_blocks_indices)
ax.set_xticklabels(age_blocks)
ax.legend()
plt.tight_layout()
plt.show()