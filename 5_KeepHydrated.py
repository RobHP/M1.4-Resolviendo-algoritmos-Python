'''
Description:
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
'''

'''
Solution:

Para resolver este problema, podemos multiplicar el tiempo dado (en horas) por la cantidad de agua que Nathan bebe por hora (0.5 litros). Luego, redondeamos el resultado hacia abajo al entero más cercano para obtener la cantidad de litros que Nathan beberá.
'''
import math

def litres(time):
    # Calcular los litros de agua que Nathan beberá
    litres_drunk = 0.5 * time

    # Redondear hacia abajo al entero más cercano
    return math.floor(litres_drunk)

# Ejemplos de uso
print(litres(3))    # Salida: 1
print(litres(6.7))  # Salida: 3
print(litres(11.8)) # Salida: 5
