'''
Description:
There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity and price (per mango), calculate the total cost of the mangoes.

Examples
mango(2, 3) ==> 6    # 2 mangoes for $3 per unit = $6; no mango for free
mango(3, 3) ==> 6    # 2 mangoes for $3 per unit = $6; +1 mango for free
mango(5, 3) ==> 12   # 4 mangoes for $3 per unit = $12; +1 mango for free
mango(9, 5) ==> 30   # 6 mangoes for $5 per unit = $30; +3 mangoes for free
'''

'''
Solution:
Para resolver este problema, necesitas calcular cuántos mangos se deben pagar y cuántos se obtendrán gratis bajo la oferta "3 por 2". La idea es dividir la cantidad de mangos en grupos de tres y pagar solo por dos en cada grupo.
'''

def mango(quantity, price):
    # Calcular el número de mangos que se pagan (2 por cada grupo de 3)
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)

    # Calcular el costo total
    total_cost = paid_mangoes * price

    return total_cost

# Ejemplos de uso
print(mango(2, 3))  # Salida: 6
print(mango(3, 3))  # Salida: 6
print(mango(5, 3))  # Salida: 12
print(mango(9, 5))  # Salida: 30
