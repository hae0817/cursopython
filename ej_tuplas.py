# EJERCICIO TUPLAS

# Crea una tupla e intenta modificar su contenido
mi_tupla = (1,2,3)
try:
    mi_tupla[0] = 4
except TypeError:
    print("No se pueden modificar las tuplas")
else:
    print("Se ha conseguido realizar la modificación:", mi_tupla)

# Crea una tupla mixta
tupla_mixta = (1, "dos", [3, 4], {5: "cinco"}, (6, 7), 8.0, True, None, {9})

# Modifica el contenido del tercer elemento
tupla_mixta[2][0] = 0
print(tupla_mixta)

# Imprime los elementos de la tupla con un loop for y su tipo
for elemento in tupla_mixta:
    print(f"{str(elemento)} => {type(elemento)}")

# Convierte la tupla_mixta a una lista e imprímela
lista_mixta = list(tupla_mixta)
print(lista_mixta)

# Modifica el elemento 1 de la lista y vuelve a pasar la lista a tupla
lista_mixta[1] = 2
tupla_mixta1 = tuple(lista_mixta)
print(tupla_mixta1)

# Crea una tupla numérica y realiza las operaciones de suma, máximo y mínimo
tupla_numerica = (8, 4, 9.1, 0.14, -2)
suma = sum(tupla_numerica)
maximo = max(tupla_numerica)
minimo = min(tupla_numerica)
print(suma, maximo, minimo)

# Calcula los cuadrados de la tupla con compresión
tupla_square = tuple(i ** 2 for i in tupla_numerica)
print(tupla_square)

# Desempaqueta la tupla en tantas variables como elementos tenga
a, b, c, d, e = tupla_numerica
print(f"Desempaquetado: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
