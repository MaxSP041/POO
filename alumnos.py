"""nombre=[]
calificacion=[]
for i in range(0,3):
    nombre.append(input("Ingrese su nombre: "))
    calificacion.append(int(input("Ingrese la calificacion: ")))
for i in range(len(nombre)):
    print(nombre[i]," su calificacion es: ",calificacion[i])
nombre=[]
calificacion=[]
r="s"
while r=="s":
    nombre.append(input("Ingrese su nombre: "))
    calificacion.append(int(input("Ingrese la calificacion: ")))
    r=input("Desea ingresar otro? ")
for i in range(len(nombre)):
    print(nombre[i]," su calificacion es: ",calificacion[i])
"""

class estudiante:
    def __init__(self):
        self.nombre = []
        self.calificacion1 = []
        self.calificacion2 = []
        self.calificacion3 = []
        self.promedio = []

    def aggEstu(self):
            self.nombre.append(input("Ingrese su nombre: "))
            self.calificacion1.append(int(input("Ingrese la calificación 1: ")))
            self.calificacion2.append(int(input("Ingrese la calificación 2: ")))
            self.calificacion3.append(int(input("Ingrese la calificación 3: ")))
            self.promedio.append((self.calificacion1[i] + self.calificacion2[i] + self.calificacion3[i]) / 3)


    def result(self,c): 
            if self.promedio[c] >= 9:
                r=(self.nombre[c]," calificación 1:",self.calificacion1[c],",  calificación 2: ",self.calificacion2[c],",  calificación 3: ",self.calificacion3[c],", promedio: ",self.promedio[c],"Felicidades, estás aprobado")
            elif self.promedio[c] >= 7:
                r=(self.nombre[c]," calificación 1:",self.calificacion1[c],",  calificación 2: ",self.calificacion2[c],",  calificación 3: ",self.calificacion3[c],", promedio: ",self.promedio[c],"Aprobado, hechale más ganas")
            else:
                r=(self.nombre[c]," calificación 1:",self.calificacion1[c],",  calificación 2: ",self.calificacion2[c],",  calificación 3: ",self.calificacion3[c],", promedio: ",self.promedio[c],"Reprobado, esfuerzate más")
            return r


estudiante = estudiante()
r="s"
i=0
while r=="s":
    estudiante.aggEstu()
    r=input("Desea ingresar otro? (s/n): ")
    i+=1
for c in range(0,i):
    r=estudiante.result(c)
    print(r)