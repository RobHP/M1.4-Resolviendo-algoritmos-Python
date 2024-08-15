'''
Description:
The aspect ratio of an image describes the proportional relationship between its width and its height. Most video shown on the internet uses a 16:9 aspect ratio, which means that for every pixel in the Y, there are roughly 1.77 pixels in the X (where 1.77 ~= 16/9). As an example, 1080p video with an aspect ratio of 16:9 would have an X resolution of 1920, however 1080p video with an aspect ratio of 4:3 would have an X resolution of 1440.

Write a function that accepts arbitrary X and Y resolutions and converts them into resolutions with a 16:9 aspect ratio that maintain equal height. Round your answers up to the nearest integer.

Example
374 × 280 pixel image with a 4:3 aspect ratio.
'''

'''
Solution:
Para resolver este problema, necesitas una función que tome las resoluciones X e Y dadas y calcule una nueva resolución X que mantenga la relación de aspecto 16:9, manteniendo la altura (Y) constante. Luego, redondea la resolución X al entero más cercano.
'''

import math

def convert_to_16_9(x, y):
    # Calcula la nueva resolución X manteniendo la altura y la relación de aspecto 16:9
    new_x = (16 / 9) * y

    # Redondea hacia arriba al entero más cercano
    new_x = math.ceil(new_x)

    # Retorna la nueva resolución
    return (new_x, y)


# Ejemplo de uso
x = 1440
y = 1080
new_resolution = convert_to_16_9(x, y)
print(new_resolution)  # Salida: (1920, 1080)
