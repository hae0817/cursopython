# EJERCICIO LISTA POR COMPRESIÓN

temperatura_celcius = [20, -150, -197, -100, -146, -200, 0, 30, -208]
lista_procesada = [temperatura for temperatura in temperatura_celcius if temperatura > -196]
print(lista_procesada)
