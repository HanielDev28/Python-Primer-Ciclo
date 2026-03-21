"---Mi Diario de Aprendizaje---"
respuesta=(input("¿Que aprendiste hoy? "))
with open("diario.txt", "a") as diario:
    diario.write("----Entrada del Diario----\n")
    diario.write(f"Hoy aprendi: {respuesta}\n")
    diario.write("-------------------------\n")
with open("diario.txt","r") as diario: 
    contenido= diario.read()
    print(f"Contenido del Diario:\n{contenido}")

    