class Productos:
    def __init__(self):
        pass
    def nombreproducto(self,n):
        r=[]
        producto=[[1,"Azucar"],[2,"Bombones"],[3,"Cigarros"],[4,"Aceite"],[5,"Jabon"]]
        for i in range(len(producto)):
            if n==producto[i][0]:
                r.append(producto[i][0])
                r.append(producto[i][1])
                return r
    def costos(self,n):
        r=[]
        costos=[[1,19,0,.3,5,.2],[2,20,.16,.3,2,.25],[3,90,.45,.3,5,.15],[4,40,.16,.3,3,.2],[5,16,0,.3,10,.1]]
        for i in range(len(costos)):
            if n==costos[i][0]:
                r.append(costos[i][0])
                r.append(costos[i][1])
                r.append(costos[i][2])
                r.append(costos[i][3])
                r.append(costos[i][4])
                r.append(costos[i][5])
                return r
class Ventas(Productos):
    def __init__(self):
        pass
    def pideDatos(self):
        d=[]
        d.append(int(input("Ingrese el codigo del producto: ")))
        d.append(int(input("Cantidad a comprar: ")))
        return d
    def calcularCostos(self,d):
        nombre=[]
        costos=[]
        nombre.append(self.nombreproducto(d[0]))
        costos.append(self.costos(d[1]))
        if d[1]>=costos[4]:
            subtotal=(d[1]*costos[1])
            ganancia=subtotal*costos[5]
            impuesto=ganancia*costos[2]
            precioDeVenta=ganancia+costos+impuesto
            print(d[0],nombre[1],"Total a pagar: ",precioDeVenta)
            
obj=Ventas()
obj.calcularCostos(obj.pideDatos())