import pandas as pd

datos = {
    'Producto': ['Manzana', 'Banana', 'Naranja', 'Uva', 'Pera'],
    'Precio': [1.2, 0.8, 1.0, 2.5, 1.5]
}
df = pd.DataFrame(datos)

productos_caros = df[df['Precio'] > 1.0]

print("\nProductos con precio mayor a 1.0:")
print(productos_caros)