
#Bloque: Estructuras de Datos

print("Hello, World!")
#El Perfil Del Futuro Programador
nombre = "Haniel"
edad= 16  
tengo_vs_code = True 
lenguaje_favorito = input("Qué leguaje estas aprendiendo?")
print(nombre.upper())
print((len(nombre)))
frase_final= f"Hola mi nombre es {nombre} y tengo {edad} años, estoy dandole duro a {lenguaje_favorito}."
print(frase_final)
print(lenguaje_favorito * 10)

#La tienda de videojuegos
nombre= input("Dime el nombre de un juego:")
precio= float(input("Cual es el precio del juego?"))
cantidad= int(input("Cuantas unidades quieres comprar?"))
total= precio * cantidad
descuento = total - 5
print(nombre.lower())
print(len(nombre))
factura= f"Pedido: {nombre.upper()}. El total con descuento de mentor es:${descuento} "
print(factura)

#Tu colección de Steam
mi_coleccion= ["Valorant", "minecraft", "roblox"] 
mi_coleccion.append(input("Dime el nombre de un juego que quieras agregar a tu colección:"))
print("El primer juego en la lista es", mi_coleccion[0])
mi_coleccion[1] = "Python Pro"
print("Ahora tengo,", len(mi_coleccion), "juegos en mi colección.")
print(mi_coleccion)

#El mapa del tesoro
posicion_tesoro= (10.5 , 20.8)
inventario_jugador= ["Espada", "Escudo"]
inventario_jugador.append("Poción ")
posicion_tesoro[0] = 5.0

programador  = {
    "nombre": "Haniel",
    "lenguaje": "Python",
    "nivel": "Principiante",
    "horas_estudio" : 2 
}
programador["horas_estudio"] = 4
programador["meta"] = "Ser Senior"
imprime= f"Soy {programador['nombre']} y mi meta es ser {programador['meta']} en {programador['lenguaje']}."
print(imprime)