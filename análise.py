#Importando Bibliotecas
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Carregando Dados
df_csv = pd.read_csv("Base Varejo.csv", sep=";")
pd.read_csv("Base Varejo.csv", encoding="utf-8")   #→ encoding
print("CSV carregado")
print(df_csv)

#Conhecendo os Dados (número de registros, colunas e tipos de dados)
print(df_csv.info())

#Estatísticas Descritivas
print(df_csv.describe(include='all'))

# Inspecionando Dados
print(df_csv.head(3))      # primeiras 3 linhas
print()
print(df_csv.tail(3))      # últimas 3 linhas
print()

#Verificando Nulos por Coluna
print(df_csv.isnull().sum())  # contagem de valores nulos por coluna
print(df_csv.isnull().mean()*100)

#Tratando categorias inválidas e vazias
df_csv['PR_CAT'] = df_csv['PR_CAT'].apply(
    lambda x: "Sem Categoria" if pd.isna(x) or x == "#N/D" else x
)

#Convertendo Strings Vazias
df_csv = df_csv.replace({'Null':np.nan, 'N/A':np.nan, '':np.nan})
print(df_csv.isnull().sum())

#Removendo Colunas Vazias com if/else
for coluna in df_csv.columns:
    if df_csv[coluna].isnull().all():
        df_csv = df_csv.drop(columns=[coluna])
        print(f"Coluna '{coluna}' removida — estava vazia")
    else:
        print(f"Coluna '{coluna}' mantida ✅")

print("\nShape final:", df_csv.shape)
print("Colunas restantes:", df_csv.columns.tolist())

#Verificando LInhas Duplicadas
print(df_csv.duplicated().sum())

#Removendo Duplicatas
print("Antes:", df_csv.shape)
df_csv = df_csv.drop_duplicates(keep='first')
print("Depois:", df_csv.shape)

#Inconsistências
print(df_csv['DATA'].head()) #datas inválidas
print(df_csv.isna()) #categorias vazias

#Convertendo Data para Datetime
df_csv['DATA'] = pd.to_datetime(df_csv['DATA'], errors='coerce')
print(df_csv['DATA'].head())

#Padronizando Colunas de Texto
colunas_texto = df_csv.select_dtypes(include="object").columns
for col in colunas_texto:
    df_csv[col] = df_csv[col].str.capitalize()

#Estatísticas Descritivas para a Coluna Número de Filhos
print(df_csv['CL_FHL'].describe())
print("Moda:", df_csv['CL_FHL'].mode()[0])

#Padrões de Agrupamento
#Agrupamento por Categoria
pivot = df_csv.pivot_table(
    values='PR_ID',
    index='PR_CAT',
    columns='CL_GENERO',
    aggfunc='count',
    fill_value=0
)

print(pivot)

#Agrupamento Número e Média de Filhos por Gênero
resumo_genero = df_csv.groupby("CL_GENERO").agg(
    Quantidade=("PR_ID", "count"),
    Media_Filhos=("CL_FHL", "mean"),
).sort_values("Quantidade", ascending=False)

print(resumo_genero)


#Gráfico Vendas por Gênero

vendas_gen = df_csv.groupby('CL_GENERO')['PR_ID'].count()

fig, ax = plt.subplots(figsize=(6, 5))
ax.bar(vendas_gen.index, vendas_gen.values, color=['salmon', 'steelblue'])

# Títulos
ax.set_title('Vendas por Gênero')
ax.set_xlabel('Gênero')
ax.set_ylabel('Quantidade')

# Valores em cima das barras
for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        int(bar.get_height()),
        ha='center', va='bottom'
    )

plt.tight_layout()
plt.savefig('grafico_genero.png', dpi=150, bbox_inches='tight')
plt.show()

import matplotlib.pyplot as plt

# Gráfico Vendas por Categoria
vendas_cat = df_csv.groupby('PR_CAT')['PR_ID'].count().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(vendas_cat.index, vendas_cat.values, color='purple')

# Títulos
ax.set_title('Quantidade de Vendas por Categoria')
ax.set_xlabel('Categoria')
ax.set_ylabel('Quantidade')

# Valores em cima das barras
for bar in ax.patches:
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        int(bar.get_height()),
        ha='center', va='bottom'
    )

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('grafico_categorias.png', dpi=150, bbox_inches='tight')
plt.show()

# Salvar dados limpos em novo CSV
df_csv.to_csv("Base_Varejo_Limpa.csv", index=False, sep=";")
print("Arquivo salvo com sucesso!")
print(df_csv.shape)



