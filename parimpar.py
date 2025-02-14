class operacion:
    def paroimpar(self,val1):
        r=""
        if (val1%2)==0:
            r="es par"
        else:
            r="es impar"
        return (r)    
    def primo(self,val1):
        r=""
        if val1>1:
            for i in range(2,val1):
                if (val1 % i)==0:
                    r=" y no es primo"
                else:
                    r=" y es primo"          
        return(r)
obj=operacion()
n=int(input("Ingrese un numero: "))
resul=obj.paroimpar(n)+obj.primo(n)
print("El numero",n,resul)