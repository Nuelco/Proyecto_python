import sqlite3
import json
import os


# 1- SQL CON SQLITE
conn=sqlite3.connect('tienda.db')
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
               id INTEGER PRIMARY KEY,
               nombre TEXT,
               edad INTEGER,
               email TEXT)''')

# Insertar clientes

cursor.execute("INSERT INTO clientes (nombre, edad, email) VALUES (?, ?, ?)",
               ('Juan Perez', 30, 'juan.perez@example.com'))
cursor.execute("INSERT INTO clientes (nombre, edad, email) VALUES (?, ?, ?)",
               ('Maria Gomez', 25, 'maria.gomez@example.com'))  
conn.commit()

# Consultar clientes
cursor.execute("SELECT * FROM clientes")
clientes_sql = cursor.fetchall()
print("Clientes en SQL:")   
for cliente in clientes_sql:
    print(cliente)  
print(os.path.abspath("tienda.db"))
conn.close()

# 2- NOSQL CON JSON
clientes_nosql = [
    {"id": 1, "nombre": "Juan Perez", "edad": 30, "email": "juan.perez@example.com", "pedidos": ["libro", "lapiz"]},
    {"id": 2, "nombre": "Ana", "edad": 25, "email": "Ana.gomez@example.com", "pedidos": ["cuaderno"]}
]

# Guardar en archivo JSON
with open('clientes.json', 'w') as file:
    json.dump(clientes_nosql, file, indent=4)
# Leer desde archivo JSON
with open('clientes.json', 'r') as file:
    clientes_json = json.load(file)
print("Clientes en NoSQL (JSON):")
for cliente in clientes_json:
    if cliente['nombre'] == "Ana":
        print(cliente['nombre'], cliente['email'], cliente['pedidos'])
print(os.path.abspath("clientes.json"))

