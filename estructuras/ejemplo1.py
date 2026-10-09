#Estructuras en python 
milista = [1,2,3,4,5]
print(milista)
print(type(milista))


miconjunto = {1,2,3,4,5}
print(miconjunto)
print(type(miconjunto))

nuevoconjunto = set(milista)
print(nuevoconjunto)

mitupla = (1,2,3,4,5)
print(mitupla[0])
print(mitupla[1])
print(mitupla)

lista = []
lista.append(mitupla)
lista.append(milista)
lista.append(miconjunto)
print(lista)


diccionario = {
 "palabra": "tula",
 "significado": "persona chismosa",
 "pais": "Nicaragua"
}
print(diccionario)

lista.append(diccionario)   

print(diccionario["palabra"])
print(diccionario["significado"])
