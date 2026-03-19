#Día 4: Las clases y objetos


class Perro: 
    def __init__(self, nombre, raza,):
        self.nombre = nombre
        self.raza = raza
        self.edad = 0
    def ladrar(self):
        return "El perro " + self.nombre + "esa ladrando: ¡Guau!"
    def cumplir_años(self, edad):
        self. edad += 1
        return f"!Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años."
        
Perro1 = Perro("Luca", "Labrador")
Perro2 = Perro("Max", "Bulldog")
print (Perro1.ladrar())
print(Perro2.ladrar()) 

print(f"Edad de {Perro1.nombre}: {Perro1.edad}")
print(Perro1.cumplir_años())
print(f"Edad de {Perro1.nombre} después de cumplir años: {Perro1.edad}")

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, monto):
        self.saldo += monto
        return f"Has depositado ${monto}. Saldo actual: ${self.saldo}."
    def retirar(self, monto):
         if monto > self.saldo:
            return "Fondos insuficientes."
         else:
            self.saldo -= monto
            return f"Has retirado ${monto}. Saldo actual: ${self.saldo}."

mis_clientes = [
   CuentaBancaria ("Haniel", 100),
    CuentaBancaria("Sofia", 200),
    CuentaBancaria("Mateo", 300)
]
for cliente in mis_clientes:
    print(cliente.depositar(50))
for cliente in mis_clientes:
    print(f"cliente: {cliente.titular}, saldo final:  ${cliente.saldo}")
    