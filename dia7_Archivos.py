from producto import Producto
from calculos import aplicar_Descuento
laptop = Producto("Laptop", 1500, 200)
def procesar_venta (producto_objeto):
    print(producto_objeto.mostrar_info())
    precio_final = aplicar_Descuento(producto_objeto.precio, producto_objeto.descuento_fijo)
    print(f"Precio final después de aplicar el descuento: ${precio_final:,.2f}")
with open("ticket_venta. txt", "w") as ticket:
    ticket.write("---- Ticket de Venta ----\n")
    ticket.write(f"Producto: {laptop.nombre}\n")
    ticket.write(f"Precio Original: ${laptop.precio:,.2f}\n")
    precio_final = aplicar_Descuento(laptop.precio, laptop.descuento_fijo)
    ticket.write(f"Precio Final despues del Descuento: ${precio_final:,.2f}\n")
    ticket.write("--------------------------\n")