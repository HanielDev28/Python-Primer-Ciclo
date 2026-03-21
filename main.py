from inventario import Producto 
catalogo = [
    Producto("Laptop", 1000, 10),
    Producto("Teclado", 50, 20),
    Producto("Mouse", 25, 30)
]

while True:
    print("\n--- Catálogo de Productos ---")
    for i, producto in enumerate(catalogo):
        print(f"{i}. {producto.nombre} - Stock: {producto.stock}")
    try :
        opcion = int(input(" Seleeciona el numero del producto: "))
        if opcion == 3: break 
        if opcion < 0 or opcion >= len(catalogo):
            raise ValueError("Esa opcion no existe en el catalogo.")
        cantidad = int(input(f"¿Cuantas unidades de {catalogo[opcion].nombre} deseas comprar? "))
        seleccionado = catalogo [opcion]
        mensaje_exito = seleccionado.vender (cantidad)
        seleccionado.stock -= cantidad 
        print(mensaje_exito)
        with open("registro_ventas.txt", "a") as registro:
            registro.write("---- Registro de Ventas ----\n")
            registro.write("Venta realizada:\n")
            registro.write(f"Venta: {cantidad}x {seleccionado.nombre} | Total: ${seleccionado.precio * cantidad}\n")
            registro.write("-----------------------------\n")
        with open("registro_ventas.txt", "r") as registro:
            contenido = registro.read()
            print(f"Contenido del Registro de Ventas:\n{contenido}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")



    
            