class Alumnos():
    def Cantidades(self,sexos,i):
        tot=0
        if i==1:
            tot=len(sexos)
        elif i==2:
            for i in range(len(sexos)):
                if sexos[i]=="h":
                    tot+=1
        elif i==3:
            for i in range(len(sexos)):
                if sexos[i]=="m":
                    tot+=1
        return(tot) #return cantidades alumnos,hombres y mujeres
            
    def PromEd(self,edades,totA):
        promEdad=0
        for i in range(totA):
            promEdad+=edades[i]
        return(promEdad/totA) #return promedio de edades
    
    def promH(self,sexos,edades,totA,totH):
        promHom=0
        for i in range(totA):
            if sexos[i]=="h":
                promHom+=edades[i]
        return(promHom/totH) #return promedio de hombres
    
    def promM(self,sexos,edades,totA,totM):
        promMuj=0
        for i in range(totA):
            if sexos[i]=="m":
                promMuj+=edades[i]
        return(promMuj/totM) #return promedio de mujeres
        

obj=Alumnos()
r="s"
nomAlum=[]
edades=[]
sexos=[]

while r=="s":
    nomAlum.append(input("Ingresa tu nombre: "))
    edades.append(int(input("Ingresa tu edad: ")))
    sexos.append(input("Ingresa tu sexo(h/m): "))
    r=input("Desea ingresar otro?(s/n): ")
    
for i in range(1,4):
    if i==1:
        totA=obj.Cantidades(sexos,i)
    elif i==2:
        totH=obj.Cantidades(sexos,i)
    else:
        totM=obj.Cantidades(sexos,i)         
promEdad=obj.PromEd(edades,totA)
promHom=obj.promH(sexos,edades,totA,totH)
promMuj=obj.promM(sexos,edades,totA,totM)

print("El total de alumnos es ",totA," y el promedio de edades son ",promEdad)
print("El total de hombres es ",totH," y el promedio de edades son ",promHom)
print("El total de mujeres es ",totM," y el promedio de edades son ",promMuj)





