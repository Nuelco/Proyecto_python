#VARIABLE: Una variable es un espacio en la memoria que se utiliza para almacenar datos. 
# En Python, no es necesario declarar el tipo de dato de una variable, ya que el lenguaje lo infiere automáticamente.

edad= 25  # Variable de tipo entero
precio = 19.99  # Variable de tipo flotante
nombre = "Manuel"  # Variable de tipo cadena
es_estudiante = True  # Variable de tipo booleano
#TIPOS DE DATOS: Los tipos de datos más comunes en Python son:
# Enteros (int): Números sin decimales.
# Flotantes (float): Números con decimales.
# Cadenas (str): Texto.
# Booleanos (bool): Valores de verdad (True o False).
#Operadores: Los operadores son símbolos que se utilizan para realizar operaciones sobre los datos.
# Aritméticos: +, -, *, /, %, **, //
suma = 5 + 3  # Resultado: 8
resta = 10 - 2  # Resultado: 8
multiplicacion = 4 * 2  # Resultado: 8
division = 16 / 2  # Resultado: 8.0
modulo = 17 % 3  # Resultado: 2
exponente = 2 ** 3  # Resultado: 8
division_entera = 17 // 3  # Resultado: 5
# Comparación: ==, !=, >, <, >=, <=
es_igual = (5 == 5)  # Resultado: True
es_diferente = (5 != 3)  # Resultado: True
es_mayor = (7 > 3)  # Resultado: True
es_menor = (2 < 5)  # Resultado: True
es_mayor_igual = (5 >= 5)  # Resultado: True
es_menor_igual = (3 <= 4)  # Resultado: True
# Lógicos: and, or, not
es_verdadero = (True and False)  # Resultado: False
es_falso = (True or False)  # Resultado: True
no_es_verdadero = not True  # Resultado: False
#Asignación: =, +=, -=, *=, /=, %=
x = 10
x += 5  # Equivalente a x = x + 5, ahora x es 15
x -= 3  # Equivalente a x = x - 3, ahora x es 12
x *= 2  # Equivalente a x = x * 2, ahora x es 24
x /= 4  # Equivalente a x = x / 4, ahora x es 6.0
x %= 4  # Equivalente a x = x % 4, ahora x es 2.0

#Calculos simples
suma_EDAD = edad+10
print("La suma de la edad más 10 es:", suma_EDAD)

multiplicacion = precio * 2
print("El precio multiplicado por 2 es:", multiplicacion)

#Listas: Las listas son estructuras de datos que permiten almacenar múltiples valores en una sola variable.
nombres = ["Manuel", "Laura", "Pedro"]
edades = [25, 30, 22]

#Mostrar datos de Listas
print("Nombre:", nombres)
print("Edad:", edades)
print("Primer nombre de la lista:", nombres[0])  
#Modificar datos de Listas
nombres[0]='Ana'
print("Nombres estudiantes despues del cambio de la primera posicion:", nombres)

#Bucles: Los bucles se utilizan para repetir un bloque de código varias veces.
# Bucle for
for nombre_for in nombres:
    print("Nombre del estudiante for:", nombre_for)
# Bucle while
contador=0
while contador <3:
    print("Contador while:", contador)
    contador += 1
#Comentarios: Los comentarios son líneas de texto que se utilizan para explicar el código.
# En Python, los comentarios comienzan con el símbolo # y se extienden hasta el final de la línea.
# Este es un comentario de una sola línea



"""
Este es un comentario
de múltiples líneas
que se utiliza para explicar
bloques de código más grandes.
"""

#Buenas prácticas:
# Utiliza nombres descriptivos para las variables.
# Mantén el código limpio y bien organizado.
# Añade comentarios para explicar partes complejas del código.
# Sigue las convenciones de estilo de Python (PEP 8).
# Evita el uso de variables globales innecesarias.
# Prueba y depura tu código regularmente para asegurarte de que funciona correctamente.
# Utiliza funciones para organizar el código en bloques reutilizables.
# Mantén el código simple y evita la complejidad innecesaria.
# Usa herramientas de control de versiones para gestionar los cambios en el código.
# Documenta tu código para facilitar su comprensión por otros desarrolladores.
# Mantente actualizado con las mejores prácticas y nuevas características del lenguaje Python.
# Revisa y refactoriza el código periódicamente para mejorar su calidad y rendimiento.
# Evita la duplicación de código mediante la reutilización de funciones y módulos.
# Realiza pruebas unitarias para asegurar la funcionalidad de componentes individuales del código.
# Colabora con otros desarrolladores y participa en revisiones de código para mejorar la calidad del software.
# Utiliza entornos virtuales para gestionar las dependencias del proyecto.
# Mantén un estilo de codificación consistente en todo el proyecto.
# Usa bibliotecas y frameworks confiables para acelerar el desarrollo y mejorar la calidad del código.
# Prioriza la legibilidad del código sobre la optimización prematura.
# Asegúrate de manejar adecuadamente los errores y excepciones en el código.
# Realiza revisiones de seguridad para proteger el código contra vulnerabilidades.
# Mantén una buena comunicación con el equipo de desarrollo para asegurar la coherencia en el proyecto.
# Utiliza herramientas de análisis estático para identificar posibles problemas en el código.
# Documenta las decisiones de diseño y arquitectura del código para futuras referencias.
# Participa en la comunidad de desarrolladores para aprender y compartir conocimientos sobre buenas prácticas en Python.
# Siempre busca oportunidades para mejorar tus habilidades de programación y conocimiento del lenguaje Python.