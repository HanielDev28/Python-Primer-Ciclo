class Producto:
    def __init__ ( self, nombre, precio, descuento_fijo):
        self.nombre = nombre
        self.precio = precio
        self.descuento_fijo = descuento_fijo
    def mostrar_info (self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Descuento : ${self.descuento_fijo}"
    