import sqlite3
conexion = sqlite3.connect("mi_tienda.db")
cursor = conexion.cursor()
while True:
    print("\n--- Menú de Gestión de Productos ---")
    print("1. Registrar nuevo producto")
    print("2. Consultar producto")
    print("3. Eliminar producto")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        nombre = input("Ingresa el nombre del producto: ")
        precio = float(input("Ingresa el precio del producto: "))
        stock = int(input("Ingresa la cantidad que deseas: "))
        cursor.execute ("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", (nombre, precio, stock))
        conexion.commit ()
        print (f"Producto '{nombre}' registrado exitosamente con precio ${precio} y stock {stock}.")
    elif opcion == "2":
        nombre = input("Ingresa el nombre del producto que deseas consultar: ")
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
        producto = cursor.fetchone()
        if producto :
            print (f" Precio: {producto[2]}, Stock: {producto[3]}")
        else:    print("Lo sentimos. Producto no encontrado.")
        conexion.commit()
    elif opcion == "3":
        nombre = input("Ingresa el nombre del producto que deseas eliminar: ")
        cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre))
        cursores = cursor.rowcount
        if cursores > 0:
            print(f"Producto '{nombre}' eliminado exitosamente.")
        conexion.commit()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")