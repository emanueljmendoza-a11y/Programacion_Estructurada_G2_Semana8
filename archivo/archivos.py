#Leer un archivo llamodo datos.txt
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(archivo.read())
archivo.close()