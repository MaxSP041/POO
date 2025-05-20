import pandas as pd

datos = {
    'Producto': ['Manzana', 'Banana', 'Naranja', 'Uva', 'Pera'],
    'Precio': [1.2, 0.8, 1.0, 2.5, 1.5]
}
df = pd.DataFrame(datos)

print("\nPrimeras 2 filas del DataFrame de productos:")
print(df.head(2))