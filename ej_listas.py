# EJERCICIO LISTAS

# Crea la lista original
empleados = [
    ["Pedro", ["Python", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

# Haz una copia superficial y una copia profunda
import copy
copia_superficial = empleados.copy()
copia_profunda = copy.deepcopy(empleados)
print("Original: ", copia_superficial)
print("Deep Copia: ", copia_profunda)

# Modifica las Habilidades de un empleado
empleados[0][1][0] = "XML"
empleados[0][1].append("C++")
print("Original: ", copia_superficial)
print("Deep Copia: ", copia_profunda)

# Añade a Alejandro la habilidad "Java"
copia_profunda[-1][-1].append("Java")

# Imprime la lista Deep copy
print("Deep Copia Modificada: ", copia_profunda)
