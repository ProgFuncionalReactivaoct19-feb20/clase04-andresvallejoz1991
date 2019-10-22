"""
andresvallejoz1991
Encontrar la siguiente estructura
[("a",(30,1)),("b",(100,2)),("c",(20,4))]
"""
lista=[(100,2),(20,4),(30,1)]#lista 1

lista2= ["b","a","c"]#Lista 2

#Print con todas con la funcion lambda de la primera lista y el sorted de las egundo junto al zip y al list
print(list(zip(sorted(lista2),sorted(lista, key=lambda x: x[1]))))


