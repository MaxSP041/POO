class Padre: 
    def __init__(self, atributo_padre): 
        self.atributo_padre = atributo_padre 
    def metodo_padre(self): 
        return "Método padre" 
class Hija(Padre): 
    def __init__(self, atributo_hija, atributo_padre): 
        Padre.__init__(self, atributo_padre) 
        self.atributo_hija = atributo_hija 
    def metodo_hija(self): 
        return "Método hija" 
class Padre1: 
    def metodo_padre1(self): 
        return "Método padre 1" 
class Padre2: 
    def metodo_padre2(self): 
        return "Método padre 2" 
class Hija(Padre1, Padre2): 
    pass 
class ClasePadre: 
class ClaseHijo: 
def __init__(self, valor): 
self.valor = valor 
def display(self): 
print(self.valor) 
nested_obj = ClasePadre.ClaseHijo(10) 
nested_obj.display() # Output: 10 