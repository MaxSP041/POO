class clase:
    def __init__(self):
        pass
    def arrAlum(self):  
        alumnos=[]
        s="s"
        while s=="s":
            datos=[]
            nombre=input("ingrese su nombre:")
            edad=int(input("ingrese su edad:"))
            datos.append(nombre)
            datos.append(edad)
            alumnos.append(datos)
            s=input("desea agregar otro alumno?(s/*)")
        return alumnos
    def alumnMayores(self,alumnos):
        mayorEdad=[]
        for i in alumnos:
            datos=[]
            if i[1]>=18:
                datos.append(i[0])
                datos.append(i[1])
                mayorEdad.append(datos)
        return mayorEdad
    def dosalumnosmayores(self,mayorEdad):
        dosMayores=[]
        alumnoMayor1=0
        alumnoMayor2=0
        numMayor1=0
        numMayor2=0
        for i in mayorEdad:
            if i[1] > numMayor1:
                numMayor2 = numMayor1  
                numMayor1 = i[1]      
                alumnoMayor2 = alumnoMayor1
                alumnoMayor1 = i
            elif i[1] > numMayor2:
                numMayor2 = i[1]    
                alumnoMayor2 = i
        dosMayores.append(alumnoMayor1)
        dosMayores.append(alumnoMayor2)
        return dosMayores
    def impr(self,alumnos,mayorEdad,dosMayores):
        print(alumnos)
        print(mayorEdad)
        print(dosMayores)


obj=clase()
alumnos=obj.arrAlum()
mayorEdad=obj.alumnMayores(alumnos)
dosMayores=obj.dosalumnosmayores(mayorEdad)
obj.impr(alumnos,mayorEdad,dosMayores)