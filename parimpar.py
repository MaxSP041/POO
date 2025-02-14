class operacion:
    def __init__(self):
        self.n1=0
    def op(self):
        print("""
              Que opcion quieres?
              1. Par/impar
              2. Primo
              3. Ambas
              """)
        r=int(input("Opcion: "))
        return(r)
    def paroimpar(self,val1):
        if (val1%2)==0:
            return("es par")
        else:
            return("es impar")
    def primo(self,val1):
        if val1>1:
            for i in range(2,val1):
                if (val1 % i)==0:
                    return("no es primo")
                else:
                    return("es primo")
obj=operacion()
s=obj.op()
if s==1:
    obj.n1=int(input("Ingrese un numero: "))
    resul=obj.paroimpar(obj.n1)
    print("El numero",obj.n1,resul)
elif s==2:
    obj.n1=int(input("Ingrese un numero: "))
    resul=obj.primo(obj.n1)
    print("El numero",obj.n1,resul)
elif s==3:
    obj.n1=int(input("Ingrese un numero: "))
    resul=obj.paroimpar(obj.n1)
    print("El numero",obj.n1,resul)
    resul=obj.primo(obj.n1)
    print("El numero",obj.n1,resul)