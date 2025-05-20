import pandas as pd

datos = [['Ana', 28], ['Luis', 34], ['Eva', 22]]
columnas = ['Nombre', 'Edad']
df= pd.DataFrame(datos, columns=columnas)

nombres = df['Nombre']

print("\nColumna 'Nombre':")
print(nombres)