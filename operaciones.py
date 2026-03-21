
from banco import banco_seguro
cuenta_segura = banco_seguro("Carlos", 100)
print (cuenta_segura.depositar(50))
print(f"Saldo actual: ${cuenta_segura.saldo}.")

from banco import banco_seguro
from utilidades import saludo_formal    
cliente = banco_seguro("Carlos", 100)
print(saludo_formal(cliente.titular))
print(cliente.depositar(50))
