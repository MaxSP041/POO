class cinepolis:
    def __init__(self):
        pass
    def precios(self):
        opciones=[["Entrada cine",45],["Palomitas",80],["Combo 1",245],["Combo 3",120],["Entrada niño",30]]
        return opciones
class cinepolito(cinepolis):
    def carrit(self):
        carrito=[0,0,0,0,0]
        return carrito
    def eleccion(self,opciones):
        for i in range(len(opciones)):
            print(i+1,".",opciones[i])
        opc=int(input("Que opcion desea comprar: "))
        return opc-1
    def tota(self,carrito,opciones):
        total=0
        for i in range(len(carrito)):
            total+=(carrito[i]*opciones[i][1])
        print(total)
obj=cinepolito()
carrito=obj.carrit()
op="s"
while op=="s":
    opc=obj.eleccion(obj.precios())
    carrito[opc]+=1
    op=input("Desea agregar otra cosa al carrito? ")
obj.tota(carrito,obj.precios())

        
        