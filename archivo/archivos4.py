# Pedir datos al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
carrera = input("Ingrese su año y carrera: ")


with open("mis_datos2.txt", "w") as archivo:
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Edad: {edad}\n")
    archivo.write(f"Año y Carrera: {carrera}\n")

print("Datos guardados ")