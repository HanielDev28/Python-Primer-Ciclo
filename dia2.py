
# día 2: 
#BLOQUE: Los condionales
estudiante = {
    "nombre": "Haniel",
    "promedio": 16.5,
    "ciclo": 1
}
if estudiante ["promedio"] >= 17:
    print("¡Felicidades! Tienes una beca completa.")
elif estudiante ["promedio"] >= 14:
    print("¡Buen trabajo! Tienes media beca, sigue así")
else:
    print("Lo siento, debes pagar la pension completa este ciclo")

    #Reto final de decisiones
    if estudiante ["promedio"] >= 17 and estudiante ["ciclo"]  > 1:
        print("Usted tiene beca completa")
    elif estudiante ["promedio"] >= 14 or estudiante ["nombre"] =="Haniel":
        print("Tienes el beneficio por ser dueño del programa")
    else:
        print("No tienes nada")


invitados = ["Haniel", "Mateo", "Sofia", "Lucas","Elena"]
for invitados in invitados: 
    if invitados == "Haniel":
        print("¡Acceso concedido, Administrador!")
    else: 
        print(f"Hola, {invitados}!puedes pasar como invitado.")

saldo= 500
pin_corecto= "1234"
pin_ingresado= ""
while pin_ingresado != pin_corecto:
    pin_ingresado = input("Ingresa tu PIN:")
    if pin_ingresado == pin_corecto:
        print(f"PIN correcto. Tu saldo es.${saldo}")
        break
    else:
        print("PIN incorrecto. Intenta de nuevo.")
