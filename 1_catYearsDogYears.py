'''
Description:
I have a cat and a dog.
I got them at the same time as kitten/puppy. That was humanYears years ago.
Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:
humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that
'''

'''
Solution:
El problema de calcular la edad del gato y del perro en "años humanos" puede ser resuelto utilizando una serie de condiciones que reflejan cómo se acumulan los años de los animales a lo largo del tiempo. El objetivo es convertir una edad dada en años humanos en su equivalente en años de gato y perro según reglas específicas.
'''
def calculate_pet_ages(humanYears):
    # Inicializar las edades de gato y perro
    catYears = 0
    dogYears = 0

    # Calcular las edades de acuerdo a los años humanos
    if humanYears >= 1:
        catYears += 15
        dogYears += 15
    if humanYears >= 2:
        catYears += 9
        dogYears += 9
    if humanYears > 2:
        catYears += 4 * (humanYears - 2)
        dogYears += 5 * (humanYears - 2)

    # Retornar las edades en una lista
    return [humanYears, catYears, dogYears]


# Ejemplo de uso
humanYears = 5
ages = calculate_pet_ages(humanYears)
print(ages)  # Salida esperada: [5, 36, 39]
