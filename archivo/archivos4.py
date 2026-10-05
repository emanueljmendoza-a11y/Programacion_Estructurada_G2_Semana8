# Pedir datos al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
carrera = input("Ingrese su año y carrera: ")


with open("mis_datos2.txt", "w") as archivo:
    archivo.write(f"Nombre: {nombre}")
    archivo.write(f"Edad: {edad}")
    archivo.write(f"Año y Carrera: {carrera}")

print("Datos guardados ")