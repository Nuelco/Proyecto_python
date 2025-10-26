# CLASE: Molde base para crear moldes de objetos
# METDODOS: Funciones definidas dentro de una clase que describen el comportamiento de los objetos

print( "------------CLASE COCHE------------")
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
    def acelerar(self):
        print("El " + self.marca + " está acelerando.")

mi_coche = Coche("Toyota", "Azul")
mi_coche.acelerar()

otro_coche = Coche("Alfa Romeo", "Rojo")
otro_coche.acelerar()
print( "------------CLASE MASCOTA------------")
class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def hacer_sonido(self):
        if self.tipo == "perro":
            print(self.nombre + " dice: Guau Guau!")
        elif self.tipo == "gato":
            print(self.nombre + " dice: Miau Miau!")
        else:
            print(self.nombre + " hace un sonido desconocido.")

mi_mascota = Mascota("Nala", "perro")
mi_mascota2= Mascota("Michi", "gato")
mi_mascota3 = Mascota("Pájaro", "pájaro")
mi_mascota.hacer_sonido()
mi_mascota2.hacer_sonido()
mi_mascota3.hacer_sonido()
