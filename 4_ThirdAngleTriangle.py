'''
Description:
You are given two interior angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested.
'''

'''
Solution:
Para resolver este problema, podemos utilizar el hecho de que la suma de los tres ángulos interiores de cualquier triángulo siempre es 180 grados. Si se te dan dos ángulos, puedes encontrar el tercer ángulo restando la suma de los dos ángulos dados de 180.
'''
def find_third_angle(angle1, angle2):
    # La suma de los ángulos de un triángulo es 180 grados
    return 180 - (angle1 + angle2)

# Ejemplos de uso
print(find_third_angle(60, 60))  # Salida: 60
print(find_third_angle(45, 45))  # Salida: 90
print(find_third_angle(30, 90))  # Salida: 60
