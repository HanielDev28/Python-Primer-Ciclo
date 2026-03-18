
#Día 3: Las funciones
def saludar_usuario(nombre):
    print(f"Hola, {nombre}! Bienvenido a mi programa.")
saludar_usuario("Haniel")

def calcular_total (cuenta, propina):
    total = cuenta + (cuenta * propina)
    return total
cuenta = float(input("Ingresa el monto de tu cuenta:"))
propina = float(input("Ingresa el porcentaje de propina que deseas dejar (en decimal, por ejemplo, 0.15 para 15%):"))
print("El total con propina es:", calcular_total(cuenta, propina))


def calcular_total (cuenta, propia = 0.10):
    total = cuenta + (cuenta * propia)
    return total
print(calcular_total(50))
print(calcular_total(50, 0.20))


def verificar_estado(lista_notas): 
    promedio = sum(lista_notas) / len(lista_notas)
    
    if promedio >= 10.5:
        return "Aprobado"
    else:
        return "Reprobado"

alumno = {
    "nombre": "Haniel",
    "notas": [12, 15, 18] # Aquí van los números reales
}

resultado = verificar_estado(alumno["notas"])
print(f"El alumno {alumno['nombre']} está {resultado}.")

alumno= {
    "nombre": "Pedro",
    "notas": [8, 5, 10]
}
resultado = verificar_estado(alumno["notas"])
print(f"El alumno {alumno['nombre']} está {resultado}.")

clase= [
    {"nombre": "Haniel", "notas": [12, 15, 18]},
    {"nombre": "Pedro", "notas": [8, 5, 10]},
    {"nombre": "Sofia", "notas": [20, 19, 18]}
]
for alumno in clase:
    resultado = verificar_estado(alumno["notas"])
    print(f"El alumno {alumno['nombre']} está {resultado}.")

    #El Gran Reto Fianl:"Gestor de Nómina Tech"
    equipo= [
    {"nombre": "Haniel", "lenguaje ": "Python", "sueldo_base": 5000},
    {"nombre": "Sofia", "lenguaje": "Java", "sueldo_base": 2000},
    {"nombre": "Mateo", "lenguaje": "Python", "sueldo_base": 8000}
]
    def calcular_bono(lenguaje, sueldo):
        if lenguaje == "Python":
            return sueldo * 0.20
        else :
            return sueldo * 0.05
        
    for programador in equipo:
        bono = calcular_bono(programador["lenguaje"], programador["sueldo_base"])
        sueldo_total = programador["sueldo_base"] + bono
        print(f"{programador['nombre']}, con lenguaje {programador['lenguaje']},se le tiene que pagar ${sueldo_total} ")