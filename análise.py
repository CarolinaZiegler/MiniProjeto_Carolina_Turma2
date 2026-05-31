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


#Verificando LInhas Duplicadas
print(df_csv.duplicated().sum())

#Inconsistências
print(df_csv['DATA'].head()) #datas inválidas
print(df_csv.isna()) #categorias vazias

#Convertendo Data para Datetime
df_csv['DATA'] = pd.to_datetime(df_csv['DATA'], errors='coerce')
print(df_csv['DATA'].head())

#Convertendo Strings Vazias
df_csv = df_csv.replace({'Null':np.nan, 'N/A':np.nan, '':np.nan})
print(df_csv.isnull().sum())