"""
andresvallejoz1991
"""

paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]#Lista con la dupla de las notas
nombres = ["Ángel", "José", "Ana"]#Lista con los nombres
#funcion = tuple(map(lambda x: (x[0] + x[1] + x[2])/3, paraleloA))
print(list(zip(tuple(map(lambda x: (x[0] + x[1] + x[2])/3, paraleloA)),nombres)))#Impresion final con la funcion de promedio y los nombres
