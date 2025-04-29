class FamiliaProgramadores: 
    def __init__(self, nombre): 
        self.nombre = nombre 
    def saludar(self): 
        print("Hola, soy", self.nombre, "y soy un programador.") 
    def trabajar(self): 
        print("Estoy trabajando en un proyecto emocionante!") 
class HijoProgramador(FamiliaProgramadores): 
    def __init__(self, nombre, lenguaje): 
        super().__init__(nombre) 
        self.lenguaje = lenguaje 
    def programar(self): 
        print("Estoy programando en", self.lenguaje) 
    def jugar(self): 
        print("¡Hora de jugar a mi videojuego!") 
hijo = HijoProgramador("Juan", "Python") 
hijo.saludar()    
# Salida: Hola, soy Juan y soy un programador. 
hijo.programar()  # Salida: Estoy programando en Python 
hijo.trabajar()   # Salida: Estoy trabajando en un proyecto emocionante! 
hijo.jugar()      # Salida: ¡Hora de jugar a mi videojuego!