import sqlite3 
conexion = sqlite3.connect('mi_tienda.db')
cursor = conexion.cursor()
cursor. execute ('''CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER DEFAULT 0
)''')
cursor.execute ("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Laptop", 1000, 10))
cursor.execute ("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Mause", 25, 30))
cursor.execute ("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", ("Teclado", 50, 20))
conexion.commit()
cursor.execute("SELECT * FROM productos")
resultados = cursor.fetchall()
for fila in resultados:
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Precio: {fila[2]}, Stock: {fila[3]}")
conexion.close()

