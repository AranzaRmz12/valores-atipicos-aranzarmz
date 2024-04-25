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
#print(valores_nulos)

# -----------------------------------------------------------
# IMPORTE
# CON CUARTILES
# -----------------------------------------------------------

# HISTOGRAMA Y DIAGRAMA DE CAJA CON OUTLIERS

# Histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = df["IMPORTE"], color = 'red', rwidth = 0.50)
plt.title('Histograma de IMPORTE con outliers')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

# Diagrama de cajas
fig = plt.figure(figsize = (5, 3))
plt.boxplot(df["IMPORTE"]) 
plt.title("Boxplot de IMPORTE con outliers")
#plt.show()

# Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y = df["IMPORTE"]
#print(y)

percentile25 = y.quantile(0.25) #Q1
percentile75 = y.quantile(0.75) #Q3
iqr = percentile75 - percentile25

Limite_Superior_iqr = percentile75 + 1.5*iqr
Limite_Inferior_iqr = percentile25 - 1.5*iqr
#print("Limite superior permitido usando Cuartiles: ", Limite_Superior_iqr)
#print("Limite inferior permitido usando Cuartiles: ", Limite_Inferior_iqr)

# Obtenemos datos limpios
data_clean_iqr = df[(y <= Limite_Superior_iqr) & (y >= Limite_Inferior_iqr)]
#print(data_clean_iqr)

# HISTOGRAMA Y DIAGRAMA DE CAJA SIN OUTLIERS

# Histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = data_clean_iqr["IMPORTE"], color = 'blue', rwidth = 0.50)
plt.title('Histograma de IMPORTE sin outliers con cuartiles')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_iqr["IMPORTE"]) 
plt.title("Boxplot de IMPORTE sin outliers con cuartiles")
#plt.show()

data_clean_iqr["IMPORTE"].to_csv('IMPORTE_iqr.csv')

# -----------------------------------------------------------
# IMPORTE
# CON DESVIACIÓN ESTÁNDAR
# -----------------------------------------------------------

# Método aplicando desviación estandar. Encuentro los valores extremos
y = df["IMPORTE"]
Limite_Superior_dev_std = y.mean() + 3*y.std()
Limite_Inferior_dev_std = y.mean() - 3*y.std()
#print("Limite superior permitido usando desviación estándar: ", Limite_Superior_dev_std)
#print("Limite inferior permitido usando desviación estándar: ", Limite_Inferior_dev_std)

# Obtenemos datos limpios
data_clean_std = df[(y <= Limite_Superior_dev_std) & (y >= Limite_Inferior_dev_std)]
#print(data_clean_std)

# Realizamos el histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = data_clean_std["IMPORTE"], color = 'green', rwidth = 0.50)
plt.title('Histograma de IMPORTE sin outliers con desviación estándar')
plt.xlabel('IMPORTE')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_std["IMPORTE"]) 
plt.title("Boxplot de IMPORTE sin outliers con desviación estándar")
#plt.show()

data_clean_std["IMPORTE"].to_csv('IMPORTE_std.csv')

# -----------------------------------------------------------
# TOTAL MX
# CON CUARTILES
# -----------------------------------------------------------

# HISTOGRAMA Y DIAGRAMA DE CAJA CON OUTLIERS

# Histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = df["TOTAL MX"], color = 'red', rwidth = 0.50)
plt.title('Histograma de TOTAL MX con outliers')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()

# Diagrama de cajas
fig = plt.figure(figsize = (5, 3))
plt.boxplot(df["TOTAL MX"]) 
plt.title("Boxplot de TOTAL MX con outliers")
#plt.show()

# Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y2 = df["TOTAL MX"]
#print(y2)

percentile25_2 = y2.quantile(0.25) #Q1
percentile75_2 = y2.quantile(0.75) #Q3
iqr_2 = percentile75_2 - percentile25_2

Limite_Superior_iqr_2 = percentile75_2 + 1.5*iqr_2
Limite_Inferior_iqr_2 = percentile25_2 - 1.5*iqr_2
#print("Limite superior permitido usando Cuartiles: ", Limite_Superior_iqr_2)
#print("Limite inferior permitido usando Cuartiles: ", Limite_Inferior_iqr_2)

# Obtenemos datos limpios
data_clean_iqr_2 = df[(y2 <= Limite_Superior_iqr_2) & (y2 >= Limite_Inferior_iqr_2)]
#print(data_clean_iqr_2)

# HISTOGRAMA Y DIAGRAMA DE CAJA SIN OUTLIERS

# Histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = data_clean_iqr_2["TOTAL MX"], color = 'blue', rwidth = 0.50)
plt.title('Histograma de TOTAL MX sin outliers con cuartiles')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_iqr_2["TOTAL MX"]) 
plt.title("Boxplot de TOTAL MX sin outliers con cuartiles")
#plt.show()

data_clean_iqr_2["TOTAL MX"].to_csv('TOTAL MX_iqr.csv')

# -----------------------------------------------------------
# TOTAL MX
# CON DESVIACIÓN ESTÁNDAR
# -----------------------------------------------------------

# Método aplicando desviación estandar. Encuentro los valores extremos
y2 = df["TOTAL MX"]
Limite_Superior_dev_std_2 = y2.mean() + 3*y2.std()
Limite_Inferior_dev_std_2 = y2.mean() - 3*y2.std()
#print("Limite superior permitido usando desviación estándar: ", Limite_Superior_dev_std_2)
#print("Limite inferior permitido usando desviación estándar: ", Limite_Inferior_dev_std_2)

# Obtenemos datos limpios
data_clean_std_2 = df[(y2 <= Limite_Superior_dev_std_2) & (y2 >= Limite_Inferior_dev_std_2)]
#print(data_clean_std_2)

# Realizamos el histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = data_clean_std_2["TOTAL MX"], color = 'green', rwidth = 0.50)
plt.title('Histograma de TOTAL MX sin outliers con desviación estándar')
plt.xlabel('TOTAL MX')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_std_2["TOTAL MX"]) 
plt.title("Boxplot de TOTAL MX sin outliers con desviación estándar")
#plt.show()

data_clean_std_2["TOTAL MX"].to_csv('TOTAL MX_std.csv')

# -----------------------------------------------------------
# TOTAL SAT
# CON CUARTILES
# -----------------------------------------------------------

# HISTOGRAMA Y DIAGRAMA DE CAJA CON OUTLIERS

# Histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = df["TOTAL SAT"], color = 'red', rwidth = 0.50)
plt.title('Histograma de TOTAL SAT con outliers')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
#plt.show()

# Diagrama de cajas
fig = plt.figure(figsize = (5, 3))
plt.boxplot(df["TOTAL SAT"]) 
plt.title("Boxplot de panaderia con outliers")
#plt.show()

# Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y3 = df["TOTAL SAT"]
#print(y3)

percentile25_3 = y3.quantile(0.25) #Q1
percentile75_3 = y3.quantile(0.75) #Q3
iqr_3 = percentile75_3 - percentile25_3

Limite_Superior_iqr_3 = percentile75_3 + 1.5 * iqr_3
Limite_Inferior_iqr_3 = percentile25_3 - 1.5 * iqr_3
#print("Limite superior permitido usando Cuartiles: ", Limite_Superior_iqr_3)
#print("Limite inferior permitido usando Cuartiles: ", Limite_Inferior_iqr_3)

# Obtenemos datos limpios
data_clean_iqr_3 = df[(y3 <= Limite_Superior_iqr_3) & (y3 >= Limite_Inferior_iqr_3)]
#print(data_clean_iqr_3)

# HISTOGRAMA Y DIAGRAMA DE CAJA SIN OUTLIERS

# Histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = data_clean_iqr_3["TOTAL SAT"], color = 'blue', rwidth = 0.50)
plt.title('Histograma de TOTAL SAT sin outliers con cuartiles')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_iqr_3["TOTAL SAT"]) 
plt.title("Boxplot de TOTAL SAT sin outliers con cuartiles")
#plt.show()

data_clean_iqr_3["TOTAL SAT"].to_csv('TOTAL SAT_iqr.csv')

# -----------------------------------------------------------
# TOTAL SAT
# CON DESVIACIÓN ESTÁNDAR
# -----------------------------------------------------------

# Método aplicando desviación estandar. Encuentro los valores extremos
y3 = df["TOTAL SAT"]
Limite_Superior_dev_std_3 = y3.mean() + 3 * y3.std()
Limite_Inferior_dev_std_3 = y3.mean() - 3 * y3.std()
#print("Limite superior permitido usando desviación estándar: ", Limite_Superior_dev_std_3)
#print("Limite inferior permitido usando desviación estándar: ", Limite_Inferior_dev_std_3)

# Obtenemos datos limpios
data_clean_std_3 = df[(y3 <= Limite_Superior_dev_std_3) & (y3 >= Limite_Inferior_dev_std_3)]
#print(data_clean_std_3)

# Realizamos el histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = data_clean_std_3["TOTAL SAT"], color = 'green', rwidth = 0.50)
plt.title('Histograma de TOTAL SAT sin outliers con desviación estándar')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_std_3["TOTAL SAT"]) 
plt.title("Boxplot de TOTAL SAT sin outliers con desviación estándar")
#plt.show()

data_clean_std_3["TOTAL SAT"].to_csv('TOTAL SAT_std.csv')