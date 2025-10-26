# Diccionarios: Organizar datos en pares clave-valor

persona = {    "nombre": "Carlos",    "edad": 30,    "ciudad": "Madrid"}
print("Nombre de la persona:", persona["nombre"])
print("Edad de la persona:", persona["edad"])

# Modificar valores en el diccionario
persona["edad"] = 27  
print("Edad modificada de la persona:", persona["edad"])

# Añadir valores en el diccionario
persona["profesion"] = "Ingeniero"  # Agregar nuevo par clave-valor
print("Diccionario persona actualizado:", persona)

# Funciones: Reutilizar código
def saludar(nombre):
    print("Hola, " + nombre + "!")
saludar("María")

def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("El resultado de la suma es:", resultado)

def describir_persona(datos):
    print("Nombre: ", datos["nombre"])
    print("Edad: ", datos["edad"])

describir_persona(persona)