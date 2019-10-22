"""
andresvallejoz1991
"""
#listadoA con los numeros
listaA = [10,2,3,4]
#ListadoB con las letras
listaB = ["a","b","c","d"]
#Ordenar las listas 
listaA1= sorted(listaA, key=lambda x: x)
listaB1= sorted(listaB, reverse=True)
#Se almacenan en un zip
resultadof=list(zip(listaA1,listaB1))
#Se obtiene el maximo
ma = max(resultadof)
#Impresion final
print(resultadof)
print(ma)

