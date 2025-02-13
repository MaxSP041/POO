"""
Programa hecho por Stringhini Ponce Maximiliano el 13/02/25
"""
class figuras:
    def __init__(self):
        self.a=0
        self.b=0
        self.c=0
    def op(self):
        print("""
              Que opcion quieres?
              1. circulo
              2. trapecio
              3. rectangulo
              """)
        r=int(input("Opcion: "))
        return(r)
    def circulo(self,r):
        area=3.1416*(r**2)
        return(area)
    def trapecio(self,b1,b2,h):
        area=((b1+b2)*h)/2
        return(area)
    def rectangulo(self,b,h):
        area=b*h
        return(area)
    
obj=figuras()
s=obj.op()
if s==1:
    obj.a=float(input("Escribe radio: "))
    resultado=obj.circulo(obj.a)
    print("El area del circulo es: ",resultado)
elif s==2:
    obj.a=float(input("Escribe base 1: "))
    obj.b=float(input("Escribe base 2: "))
    obj.c=float(input("Escribe altura: "))
    resultado=obj.trapecio(obj.a,obj.b,obj.c)
    print("El area del trapecio es: ",resultado)
elif s==3:
    obj.a=float(input("Escribe base: "))
    obj.b=float(input("Escribe altura: "))
    resultado=obj.rectangulo(obj.a,obj.b)
    print("El area del rectangulo es: ",resultado)