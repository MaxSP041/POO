"""nombre=["chucho", "pepe", "pablos"]
op="s"
while op=="s":
    try:
        x=int(input("Dame un numero del 1 al 10: "))
        print(nombre[x])
        op=input("Otro?")
    except IndexError:
        print("ora no existe el ",x)"""
nombre=[]
op="s"
while op=="s":
    datos=[]
    datos.append(int(input("numero de control: ")))
    datos.append(input("nombre del alumno"))
    datos.append(input("nombre de la carrera"))
    nombre.append(datos)
    op=input("Otro?(s/n)")
    print(nombre)