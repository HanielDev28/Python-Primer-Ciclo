import sqlite3 
conexion = sqlite3.connect('mi_tienda.db')
cursor = conexion.cursor()
nombre = input("Ingresa el nombre del producto que deseas consultar: ")
cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
producto = cursor.fetchone()
if producto :
    print (f" Precio: {producto[2]}, Stock: {producto[3]}")
else:    print("Lo sentimos. Producto no encontrado.")
conexion.close()