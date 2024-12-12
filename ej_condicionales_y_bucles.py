#EJERCICIO CONDICIONALES Y BUCLES

#Generar texto de 1000 líneas
texto_largo = ["Línea " + str(i + 1) for i in range(1000)]
#Crear dos listas:
lista_bloques = [] #x bloques de 25 líneas
bloque_actual = [] #1 bloque de 25 líneas

for linea in texto_largo:
    bloque_actual.append(linea)
    if len(bloque_actual) == 25:
        lista_bloques.append(bloque_actual) #guardar el bloque cuando este alcance 25 líneas
        bloque_actual.clear() #vaciar la lista

print(f"Cantidad de bloques creados: {len(lista_bloques)}") #salida: Cantidad de bloques creados: 40
print("Primer bloque:", lista_bloques[0]) #salida: Primer bloque: ['Línea 1', 'Línea 2', ..., 'Línea 25']