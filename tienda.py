from producto import Producto
from calculos import aplicar_Descuento

laptop = Producto("Laptop", 1500, 200)
teclado = Producto("Teclado", 100, 15)

def procesar_venta (producto_objeto):
    print(producto_objeto.mostrar_info())
    precio_final = aplicar_Descuento(producto_objeto.precio, producto_objeto.descuento_fijo)
    print(f"Precio final después de aplicar el descuento: ${precio_final:,.2f}")
procesar_venta(laptop)
procesar_venta(teclado)