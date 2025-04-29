class arrAB():
    def suma(self,a,b):
        c=[]
        for i in range(len(a)):
            c.append([])
            for j in range(len(a[i])):
                c[i].append(a[i][j]+b[i][j])
        return c
    def resta(self,a,b):
        c=[]
        for i in range(len(a)):
            c.append([])
            for j in range(len(a[i])):
                c[i].append(a[i][j]-b[i][j])
        return c

    def cambioB(self,cant,cambio):
        cant2=cant
        if cant2>=500:
            cambio[0].append(math.trunc(cant2/500))
            cant2-=(cambio[0][1]*500)
        if cant2>=200:
            cambio[1].append(math.trunc(cant2/200))
            cant2-=(cambio[1][1]*200)
        if cant2>=100:
            cambio[2].append(math.trunc(cant2/100))
            cant2-=(cambio[2][1]*100)
        if cant2>=50:
            cambio[3].append(math.trunc(cant2/50))
            cant2-=(cambio[3][1]*50)
        if cant2>=20:
            cambio[4].append(math.trunc(cant2/20))
            cant2-=(cambio[4][1]*20)
        return cambio
    
    def letr(self,numLet):
        letras=[]
        for i in range(len(numLet)):
            for j in range(len(numLet[i])):
                if isinstance(numLet[i][j],str):
                    letras.append(numLet[i][j])
        return letras
    def mayor(self,numLet):
        numMay=0
        for i in range(len(numLet)):
            for j in range(len(numLet[i])):
                if isinstance(numLet[i][j],str):
                    pass
                else:
                    if numLet[i][j]>numMay:
                        numMay=numLet[i][j]
        return numMay
    def menor(self,numLet):
        numMen=numLet[0][0]
        for i in range(len(numLet)):
            for j in range(len(numLet[i])):
                if isinstance(numLet[i][j],str):
                    pass
                else:
                    if numLet[i][j]<numMen:
                        numMen=numLet[i][j]
        return numMen
#programa    
import math

#2matrices
a=[[5,6,9,67],[3,23,89,44],[45,12,7,56],[44,45,54,34]]
b=[[35,67,7,6],[43,63,8,4],[5,52,4,6],[4,65,5,4]]
obj=arrAB()
print("Matriz a: ",a)
print("Matriz b: ",b)
print("Suma de matriz a y b: ",obj.suma(a,b))
print("Resta de matriz a y b: ",obj.resta(a,b))

#cambio
cant=int(input("Cantidad a cambiar: "))
cambio=[[500],[200],[100],[50],[20]]
print("El cambio a dar de", cant," es ",obj.cambioB(cant,cambio))

#matriz letras y num
numLet=[
    [5,6,9,"Z"],
    [3,"R",89,44],
    [45,"A4",7,56],
    [44,45,"X",34],
    ["Y",5,6,7]
]
print(numLet)
print(obj.letr(numLet))
print(obj.mayor(numLet))
print(obj.menor(numLet))       
        
        

                