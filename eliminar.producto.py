import sqlite3
conexion = sqlite3.connect("mi_tienda.db")
cursor = conexion.cursor()
nombre = input("Ingresa el nombre del producto que deseas eliminar: ")
cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre))
cursores = cursor.rowcount
if cursores > 0:
    print(f"Producto '{nombre}' eliminado exitosamente.")
conexion.commit()
conexion.close()