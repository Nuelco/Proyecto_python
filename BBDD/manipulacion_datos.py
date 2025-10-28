import pandas as pd
import numpy as np

#Cargar datos del dataset
df = pd.read_csv(r"C:\Users\mzbs\Documents\Curso Python\bbdd\ventas_tienda.csv", low_memory=False)
print(df)

#Operaciones con pandas
# 1- Filtrar productos con precio mayor a 20€
productos_caros = df[df['precio'] > 20]
print("Productos con precio mayor a 20€:")
print(productos_caros)

# 2- Manejar datos faltantes: rellenar valores con 0
df['cantidad']= df['cantidad'].fillna(0)
print("Datos después de rellenar valores faltantes en 'cantidad':")
print(df)   

# 3- Calcular el ingreso total por producto (precio * cantidad)
df['ingreso_total'] = df['precio'] * df['cantidad']
print("Datos después de calcular el ingreso total por producto:")
print(df)

#Operaciones con numpy
# 4- Calcular el precio promedio 
precio_promedio = np.mean(df['precio'])
print(f"Precio promedio de los productos: {precio_promedio:.2f}€")

# 5- Calcular total de unidades vendidas
total_unidades_vendidas = np.sum(df['cantidad'])
print(f"Total de unidades vendidas: {total_unidades_vendidas}") 

