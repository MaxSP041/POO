import pandas as pd

datos = {
    'Producto': ['Manzana', 'Banana', 'Naranja', 'Uva', 'Pera'],
    'Precio': [1.2, 0.8, 1.0, 2.5, 1.5]
}
df = pd.DataFrame(datos)

dimensiones = df.shape

print("\nDimensiones del DataFrame (filas, columnas):")
print(dimensiones)
print(f"El DataFrame tiene {dimensiones[0]} filas y {dimensiones[1]} columnas.")