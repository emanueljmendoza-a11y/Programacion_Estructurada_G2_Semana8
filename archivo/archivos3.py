#Crear y Guardar un archivo
frase = input("Ingrese una frase favorita: ")

with open("frase.txt", "w") as archivo:
    archivo.write(frase)

print("Archivo creado satisfactoriamente")