"""
andresvallejoz1991
"""

lista = [(100,2),(20,4),(30,1)]#Lista con la dupla de las notas
lista2 = ["b","a","c"]#Lista con los nombres
listav2 = map(lambda x:x.upper(),lista2) #Funcion para convertir las letras en mayusculas
print(list(zip(sorted(lista, key=lambda x: x[0]),sorted(listav2,reverse=True))))#Impresion final con las funciones de lambda y de reversa

