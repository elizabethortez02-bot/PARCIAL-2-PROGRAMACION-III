
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("datos.csv")

# Funciones de inspeccion
print("PRIMEROS 5 REGISTROS")
print(df.head())

print("ULTIMOS 5 REGISTROS")
print(df.tail())

print("FILAS Y COLUMNAS")
print(df.shape)

print("NOMBRES DE COLUMNAS")
print(df.columns)

print("TIPOS DE DATOS")
print(df.dtypes)

print("INFORMACION GENERAL")
df.info()

print("ESTADISTICAS BASICAS")
print(df.describe())

# Agrupar el stock por sucursal
print("STOCK POR SUCURSAL")
print(df.groupby("Sucursal")["Stock"].sum())



import matplotlib.pyplot as plt

# Agrupar el stock por sucursal
serie = df.groupby("Sucursal")["Stock"].sum()

# Crear grafico de barras
fig, ax = plt.subplots(figsize=(8, 5))

ax.bar(serie.index, serie.values, color="blue")

ax.set_title("Stock por sucursal")
ax.set_xlabel("Sucursal")
ax.set_ylabel("Unidades disponibles")

plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
