#Importando Bibliotecas
import os
import pandas as pd
import numpy as np

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

#Convertendo Strings Vazias
df_csv = df_csv.replace({'Null':np.nan, 'N/A':np.nan, '':np.nan})
print(df_csv.isnull().sum())

#Removendo Colunas Vazias 
print("Antes:", df_csv.shape)
df_csv = df_csv.loc[:, ~df_csv.columns.str.contains("Unname")]

print("Depois:", df_csv.shape)
print(df_csv.columns)

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
colunas_texto = df_csv.select_dtypes(include='object').columns

for coluna in colunas_texto:
    df_csv[coluna] = df_csv[coluna].str.strip()
    df_csv[coluna] = df_csv[coluna].str.title()

print(df_csv.head())

#Estatísticas Descritivas para a Coluna Número de Filhos
print(df_csv['CL_FHL'].describe())