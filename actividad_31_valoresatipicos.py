import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ventas_totales_sinnulos.csv', index_col = 0)
#print(df.head())

# Checamos los tipos de datos del dataframe
#print(df.info())

valores_nulos = df.isnull().sum()
#print(valores_nulos)

# Checamos los tipos de datos del dataframe
#print(df.info())

# -----------------------------------------------------------
# ventas_totales_medio_pago
# CON CUARTILES
# -----------------------------------------------------------

# HISTOGRAMA Y DIAGRAMA DE CAJA CON OUTLIERS

# Histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = df["ventas_totales_medio_pago"], color = 'red', rwidth = 0.50)
plt.title('Histograma de ventas_totales_medio_pago con outliers')
plt.xlabel('ventas_totales_medio_pago')
plt.ylabel('Frecuencia')
#plt.show()

# Diagrama de cajas
fig = plt.figure(figsize = (5, 3))
plt.boxplot(df["ventas_totales_medio_pago"]) 
plt.title("Boxplot de ventas_totales_medio_pago con outliers")
#plt.show()

# Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y = df["ventas_totales_medio_pago"]
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
plt.hist(x = data_clean_iqr["ventas_totales_medio_pago"], color = 'blue', rwidth = 0.50)
plt.title('Histograma de ventas_totales_medio_pago sin outliers con cuartiles')
plt.xlabel('ventas_totales_medio_pago')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_iqr["ventas_totales_medio_pago"]) 
plt.title("Boxplot de ventas_totales_medio_pago sin outliers con cuartiles")
#plt.show()

data_clean_iqr["ventas_totales_medio_pago"].to_csv('ventas_totales_medio_pago_iqr.csv')

# -----------------------------------------------------------
# ventas_totales_medio_pago
# CON DESVIACIÓN ESTÁNDAR
# -----------------------------------------------------------

# Método aplicando desviación estandar. Encuentro los valores extremos
y = df["ventas_totales_medio_pago"]
Limite_Superior_dev_std = y.mean() + 3*y.std()
Limite_Inferior_dev_std = y.mean() - 3*y.std()
#print("Limite superior permitido usando desviación estándar: ", Limite_Superior_dev_std)
#print("Limite inferior permitido usando desviación estándar: ", Limite_Inferior_dev_std)

# Obtenemos datos limpios
data_clean_std = df[(y <= Limite_Superior_dev_std) & (y >= Limite_Inferior_dev_std)]
#print(data_clean_std)

# Realizamos el histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = data_clean_std["ventas_totales_medio_pago"], color = 'green', rwidth = 0.50)
plt.title('Histograma de ventas_totales_medio_pago sin outliers con desviación estándar')
plt.xlabel('ventas_totales_medio_pago')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_std["ventas_totales_medio_pago"]) 
plt.title("Boxplot de ventas_totales_medio_pago sin outliers con desviación estándar")
#plt.show()

data_clean_std["ventas_totales_medio_pago"].to_csv('ventas_totales_medio_pago_std.csv')

# -----------------------------------------------------------
# ventas_totales_grupo_articulos
# CON CUARTILES
# -----------------------------------------------------------

# HISTOGRAMA Y DIAGRAMA DE CAJA CON OUTLIERS

# Histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = df["ventas_totales_grupo_articulos"], color = 'red', rwidth = 0.50)
plt.title('Histograma de ventas_totales_grupo_articulos con outliers')
plt.xlabel('ventas_totales_grupo_articulos')
plt.ylabel('Frecuencia')
#plt.show()

# Diagrama de cajas
fig = plt.figure(figsize = (5, 3))
plt.boxplot(df["ventas_totales_grupo_articulos"]) 
plt.title("Boxplot de ventas_totales_grupo_articulos con outliers")
#plt.show()

# Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y2 = df["ventas_totales_grupo_articulos"]
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
plt.hist(x = data_clean_iqr_2["ventas_totales_grupo_articulos"], color = 'blue', rwidth = 0.50)
plt.title('Histograma de ventas_totales_grupo_articulos sin outliers con cuartiles')
plt.xlabel('ventas_totales_grupo_articulos')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_iqr_2["ventas_totales_grupo_articulos"]) 
plt.title("Boxplot de ventas_totales_grupo_articulos sin outliers con cuartiles")
#plt.show()

data_clean_iqr_2["ventas_totales_grupo_articulos"].to_csv('ventas_totales_grupo_articulos_iqr.csv')

# -----------------------------------------------------------
# ventas_totales_grupo_articulos
# CON DESVIACIÓN ESTÁNDAR
# -----------------------------------------------------------

# Método aplicando desviación estandar. Encuentro los valores extremos
y2 = df["ventas_totales_grupo_articulos"]
Limite_Superior_dev_std_2 = y2.mean() + 3*y2.std()
Limite_Inferior_dev_std_2 = y2.mean() - 3*y2.std()
#print("Limite superior permitido usando desviación estándar: ", Limite_Superior_dev_std_2)
#print("Limite inferior permitido usando desviación estándar: ", Limite_Inferior_dev_std_2)

# Obtenemos datos limpios
data_clean_std_2 = df[(y2 <= Limite_Superior_dev_std_2) & (y2 >= Limite_Inferior_dev_std_2)]
#print(data_clean_std_2)

# Realizamos el histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = data_clean_std_2["ventas_totales_grupo_articulos"], color = 'green', rwidth = 0.50)
plt.title('Histograma de ventas_totales_grupo_articulos sin outliers con desviación estándar')
plt.xlabel('ventas_totales_grupo_articulos')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_std_2["ventas_totales_grupo_articulos"]) 
plt.title("Boxplot de ventas_totales_grupo_articulos sin outliers con desviación estándar")
#plt.show()

data_clean_std_2["ventas_totales_grupo_articulos"].to_csv('ventas_totales_grupo_articulos_std.csv')

# -----------------------------------------------------------
# panaderia
# CON CUARTILES
# -----------------------------------------------------------

# HISTOGRAMA Y DIAGRAMA DE CAJA CON OUTLIERS

# Histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = df["panaderia"], color = 'red', rwidth = 0.50)
plt.title('Histograma de panaderia con outliers')
plt.xlabel('panaderia')
plt.ylabel('Frecuencia')
#plt.show()

# Diagrama de cajas
fig = plt.figure(figsize = (5, 3))
plt.boxplot(df["panaderia"]) 
plt.title("Boxplot de panaderia con outliers")
#plt.show()

# Método aplicando Cuartiles. Encuentro cuartiles 0.25 y 0.75
y3 = df["panaderia"]
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
plt.hist(x = data_clean_iqr_3["panaderia"], color = 'blue', rwidth = 0.50)
plt.title('Histograma de panaderia sin outliers con cuartiles')
plt.xlabel('panaderia')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_iqr_3["panaderia"]) 
plt.title("Boxplot de panaderia sin outliers con cuartiles")
#plt.show()

data_clean_iqr_3["panaderia"].to_csv('panaderia_iqr.csv')

# -----------------------------------------------------------
# panaderia
# CON DESVIACIÓN ESTÁNDAR
# -----------------------------------------------------------

# Método aplicando desviación estandar. Encuentro los valores extremos
y3 = df["panaderia"]
Limite_Superior_dev_std_3 = y3.mean() + 3 * y3.std()
Limite_Inferior_dev_std_3 = y3.mean() - 3 * y3.std()
#print("Limite superior permitido usando desviación estándar: ", Limite_Superior_dev_std_3)
#print("Limite inferior permitido usando desviación estándar: ", Limite_Inferior_dev_std_3)

# Obtenemos datos limpios
data_clean_std_3 = df[(y3 <= Limite_Superior_dev_std_3) & (y3 >= Limite_Inferior_dev_std_3)]
#print(data_clean_std_3)

# Realizamos el histograma
fig = plt.figure(figsize = (7, 3))
plt.hist(x = data_clean_std_3["panaderia"], color = 'green', rwidth = 0.50)
plt.title('Histograma de panaderia sin outliers con desviación estándar')
plt.xlabel('panaderia')
plt.ylabel('Frecuencia')
#plt.show()

# Realizamos diagrama de caja o bigote
fig = plt.figure(figsize = (5, 3))
plt.boxplot(data_clean_std_3["panaderia"]) 
plt.title("Boxplot de panaderia sin outliers con desviación estándar")
plt.show()

data_clean_std_3["panaderia"].to_csv('panaderia_std.csv')