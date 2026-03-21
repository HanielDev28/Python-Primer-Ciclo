class Producto: 
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def vender(self, cantidad):
        if cantidad >  self.stock:
            raise ValueError(f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}. Stock disponible: {self.stock}")
        elif cantidad < 0:
                raise ValueError("La cantidad a vender no puede ser negativa.")
            
        else:
            return f"Venta exitosa de {cantidad} unidades de {self.nombre}. Total: ${self.precio * cantidad}."


  