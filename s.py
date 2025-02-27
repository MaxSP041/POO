class holaMundo:
    def __init__(self,x,y):
        self.x=0
        self.y=0
    def a(self):
        r="hola"
        return(r)
    def b(self):
        n=input("Ingresa tu nombre: ")
        return(n)
    def c(self,n,r):
        print(r+" "+n+" Buen dia")
obj=holaMundo(0,0)
obj.c(obj.b(),obj.a())