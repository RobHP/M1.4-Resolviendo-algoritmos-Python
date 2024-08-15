'''
Description:
An NBA game runs 48 minutes (Four 12 minute quarters). Players do not typically play the full game, subbing in and out as necessary. Your job is to extrapolate a player's points per game if they played the full 48 minutes.

Write a function that takes two arguments, ppg (points per game) and mpg (minutes per game) and returns a straight extrapolation of ppg per 48 minutes rounded to the nearest tenth. Return 0 if 0.

Examples:

nba_extrap(12, 20) # 28.8
nba_extrap(10, 10) # 48
nba_extrap(5, 17) # 14.1
nba_extrap(0, 0) # 0
Notes:
All inputs will be either be an integer or float.
'''

'''
Solution:
Para resolver este problema, necesitas calcular cuántos puntos un jugador podría anotar en un juego completo de 48 minutos basado en su rendimiento actual (puntos por juego) y el tiempo promedio que juega (minutos por juego). Esto se puede lograr utilizando una simple regla de tres.
'''

def nba_extrap(ppg, mpg):
    # Verificar si los minutos por juego son 0 para evitar división por cero
    if mpg == 0:
        return 0

    # Calcular la extrapolación de puntos por 48 minutos
    extrapolated_ppg = (ppg / mpg) * 48

    # Redondear al décimo más cercano
    return round(extrapolated_ppg, 1)


# Ejemplos de uso
print(nba_extrap(12, 20))  # Salida: 28.8
print(nba_extrap(10, 10))  # Salida: 48.0
print(nba_extrap(5, 17))  # Salida: 14.1
print(nba_extrap(0, 0))  # Salida: 0

