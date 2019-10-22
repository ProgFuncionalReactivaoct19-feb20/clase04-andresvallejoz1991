"""
andresvallejoz1991
"""
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]#Lista con la dupla de las notas
nombres = ["Ángel", "José", "Ana"]#Lista con los nombres

funcion = (list(zip(tuple(map(lambda x: (x[0] + x[1] + x[2])/3, paraleloA)),nombres)))#Funcions para calcular el promedio y los nombres
print(funcion)#Impresion de la lista
print(max(funcion))#Funcion para imprimir minimo
funcion1 = reversed(funcion)
print (list(reversed(funcion)))#Impresion de la lista en reversa
