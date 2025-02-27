nombre_de_la_lista = [] 
otra_lista = list() 
lista_con_elementos = [1, 2, True, 'Hola', 5.8] 
otra_lista_con_elementos = list([4, 9, False, 'texto'])
mi_lista = ['Juan', 'Pedro', 'Laura', 'Carmen', 'Susana'] 
print(mi_lista[0]) # Muestra Juan (la primera posición es la 0) 
print(mi_lista[-1]) # Muestra Susana 
print(mi_lista[1]) # Muestra Pedro 
print(mi_lista[2]) # Muestra Laura 
print(mi_lista[-2]) # Muestra Carmen
edades = [20, 41, 6, 18, 23] 
# Recorriendo los elementos 
for edad in edades: 
    print(edad) 
# Recorriendo los índices 
for i in range(len(edades)): 
    print(edades[i]) 
# Con while y los índices 
indice = 0 
while indice < len(edades): 
    print(edades[indice]) 
    indice += 1
    
números = [] 
números.append(10) 
números.append(5) 
números.append(3) 
print(números) 
# Mostrará [10, 5, 3]

números = [] 
# Unimos la lista anterior con una nueva 
números = números + [10, 5, 3] 
print(números) 
# Mostrará [10, 5, 3]

palabras = ['hola', 'hello', 'ola'] 
palabras.pop(1) 
print(palabras) 
# Mostrará ['hola', 'ola']

palabras = ['hola', 'hello', 'hello', 'ola'] 
palabras.remove('hello') 
print(palabras) 
# Mostrará ['hola', 'hello', 'ola']

# Creamos las listas (vacías al comienzo) 
nombres = [] 
identificaciones = [] 
# Definimos un tamaño para las listas 
# Lo puedes cambiar si quieres 
res="s"
tama = 0
# Leemos los datos y los agregamos a la lista 
while res == "s":
    print("Ingrese los datos de la persona", tama + 1) 
    nombre = input("Nombre: ") 
    identificación = input("Identificación: ") 
    nombres.append(nombre) 
    identificaciones.append(identificación) 
    tama += 1
    res=input("Deseas ingresar otro nombre s/n")
# Ahora mostremos las listas 
for i in range(tama):
    print("Mostrando los datos de la persona", i + 1) 
    print("Nombre:", nombres[i]) 
    print("Identificación:", identificaciones[i])