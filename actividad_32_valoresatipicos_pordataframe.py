import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('gastos_costos_20_23.xlsx', index_col = 0)
#print(df.head())

# Checamos los tipos de datos del dataframe
#print(df.info())

# Checamos los nulos
valores_nulos = df.isnull().sum()
#print(valores_nulos)

# TRATAMIENTO DE VALORES NULOS

df["FOLIO"] = df["FOLIO"].fillna("Desconocido")
valores_nulos = df.isnull().sum()
#print(valores_nulos)

df["GASTO"] = df["GASTO"].fillna(0)
valores_nulos = df.isnull().sum()
#print(valores_nulos)

df["TC"] = df["TC"].fillna(round(df["TC"].mean(), 1))
valores_nulos = df.isnull().sum()
#print(valores_nulos)

df["IMPORTE"] = df["IMPORTE"].fillna(0.00)
valores_nulos = df.isnull().sum()
#print(valores_nulos)

df["IVA"] = df["IVA"].fillna(0.00)
valores_nulos = df.isnull().sum()
#print(valores_nulos)

df["POLIZA"] = df["POLIZA"].fillna('A123456789')
valores_nulos = df.isnull().sum()
#print(valores_nulos)

df["TIPO"] = df["TIPO"].fillna('P')
valores_nulos = df.isnull().sum()
print(valores_nulos)