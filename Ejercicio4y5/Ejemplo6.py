"""
andresvallejoz1991
"""
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]#Lista con la dupla de las notas
nombres = ["Luis", "Ángel", "José", "Ana"]#Lista con los nombres

funcion1 = tuple(map(lambda x: (x[0] + x[1] + x[2])/3, paraleloA))#Funcion con el promedio total
funcion2 =tuple(map(lambda x: (x[0] + x[1] + x[2]), paraleloA))#Funcion con la suma total
funcion = (list(zip(funcion1,funcion2,nombres)))#Lista con todos los nombres y notas
#resultado = filter(lambda x: x[2]=="Ana" or x[2]=="Ángel", funcion)
resultado = filter(lambda x: x[0] <= 5, funcion)#Filtrar los datos de los dos estudiantes
print(list(resultado))#Impresion final
