import sqlite3 
conexion = sqlite3.connect('mi_tienda.db')
cursor = conexion.cursor()
nombre_producto = input("Ingresa el nombre del producto que deseas comprar: ")
cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre_producto,))
producto = cursor.fetchone()
if producto:
    print(f"Producto encontrado: {producto[1]}, Precio: ${producto[2]}, Stock: {producto[3]}")
input_cantidad = int(input("¿Cuántas unidades deseas comprar? "))
if input_cantidad > producto[3]:
    print("Lo sentimos, no hay suficiente stock disponible.")
elif input_cantidad < 0:
    print("La cantidad a comprar no puede ser negativa.")
else:
    nuevo_stock = producto[3] - input_cantidad
    cursor.execute("UPDATE productos SET stock = stock - ? WHERE nombre = ?", (input_cantidad, nombre_producto))
    conexion.commit()
    print(f"Compra exitosa de {input_cantidad} unidades de {producto[1]}. Total: ${producto[2] * input_cantidad}. Stock restante: {nuevo_stock}")
conexion.close()