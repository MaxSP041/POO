"""
mi_lista = ['Juan', 'Pedro', 'Laura', 'Carmen', 'Susana']
x="hola mundo" 
y=list(['Juan', 'Pedro', 'Laura', 'Carmen', 'Susana'])print(mi_lista[0]) # Muestra Juan (la primera posición es la 0) 
print(mi_lista[-1]) # Muestra Susana 
print(mi_lista[1]) # Muestra Pedro 
print(mi_lista[2]) # Muestra Laura 
print(mi_lista[-2]) # Muestra Carmen 
print(mi_lista[-3]) # Muestra Carmen 
print(mi_lista[-2]) # Muestra Carmen print(len(mi_lista))
print(len(x))
print(len(y))
"""
edades = [20, 41, 6, 18, 23] 
# Recorriendo los elementos 
#for edad in edades: 
    #print(edad)
#print(edades)
for i in range(1,len(edades),2):
    print(edades[i])