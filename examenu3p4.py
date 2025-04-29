class maquinita:
    def __init__(self):
        pass
    def arrprod(self):
        productos=[["pepsi",15],["coca",20],["fanta",16],["cocaBacardi",28],["peñafiel",19]]
        return productos
    def cantpro(self,productos):
        carrito=[0,0,0,0,0]
        op="s"
        while op=="s":
            print("1)pepsi=15 | 2)coca=20 | 3)fanta=16 | 4)cocaBacardi=28 | 5)peñafiel=19")
            produ=int(input("ingrese el producto que desea comprar: "))
            carrito[produ-1]+=1
            op=input("Desea agregar otro producto?(s/n)")
        return carrito
    def cambio(self,productos,carrito):
        tot=0
        for i in range(0,5):
            print("el producto ",productos[i]," se ha comprado", carrito[i]," veces")
            tot+=(productos[i][1]*carrito[i])
        print("el total de su carrito es: ",tot)
        dinero=int(input("ingrese su dinero: "))
        rest=tot-dinero
        monedas=[[10],[5],[1]]
        monedas[0].append(((math.trunc(rest/10))))
        rest-=(monedas[0][1]*10)
        monedas[1].append(((math.trunc(rest/5))))
        rest-=(monedas[1][1]*5)
        monedas[2].append(rest/1)
        rest-=monedas[1][1]
        for i in monedas:
            i[1]=abs(i[1])
        print(monedas)

import math
obj=maquinita()
productos=obj.arrprod
s="s"
while s=="s":
    carrito=obj.cantpro(productos)
    obj.cambio(productos,carrito)
    s=input("desea hacer otra compra")
    
    


