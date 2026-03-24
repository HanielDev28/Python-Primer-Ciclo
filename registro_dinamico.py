import sqlite3
conexion = sqlite3.connect("mi_tienda.db")
cursor = conexion.cursor()
try:
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    stock = int(input("Ingresa la cantidad que deseas: "))

    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if stock < 0:
        raise ValueError("La cantidad no puede ser negativa.")
except ValueError as e:
        print(f"Error: {e}")
except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
cursor.execute ("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", (nombre, precio, stock))
conexion.commit ()
print (f"Producto '{nombre}' registrado exitosamente con precio ${precio} y stock {stock}.")
conexion.close()