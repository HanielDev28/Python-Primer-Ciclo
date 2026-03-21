
#Día 5: Manejo de excepciones
#Retiro Bancario: 
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes.")
        self.saldo -= monto
        return f"Retiro exitoso. Saldo actual: ${self.saldo}."
try: 
    cuenta = CuentaBancaria("Ana", 100)
    print(cuenta.retirar(150))  
except ValueError as e:    
    print(f"Error bancario: {e} ")

class banco_seguro:
    def __init__ (self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes para el retiro.")
        elif monto < 0:
            raise ValueError("El monto de retiro no puede ser negativo.")
        
        self.saldo -= monto

        return f"Retiro exitoso. Saldo actual: ${self.saldo}."

cuenta_segura = banco_seguro("Carlos", 100)
try:
    print(cuenta_segura.retirar(500))
except ValueError as e:
    print(f"Alerta del Banco: {e}")