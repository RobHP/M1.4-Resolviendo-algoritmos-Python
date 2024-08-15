'''
Description:
Create a function that converts US dollars (USD) to Chinese Yuan (CNY) . The input is the amount of USD as an integer, and the output should be a string that states the amount of Yuan followed by 'Chinese Yuan'

Examples (Input -> Output)
15  -> '101.25 Chinese Yuan'
465 -> '3138.75 Chinese Yuan'
The conversion rate you should use is 6.75 CNY for every 1 USD. All numbers should be represented as a string with 2 decimal places. (e.g. "21.00" NOT "21.0" or "21")
'''

'''
Solution:
Para resolver este problema, puedes escribir una función en Python que convierta una cantidad dada de dólares estadounidenses (USD) a yuanes chinos (CNY) utilizando la tasa de conversión de 6.75 CNY por 1 USD. Luego, el resultado se formatea como una cadena con dos decimales, seguida de la frase "Chinese Yuan".
'''
def usd_to_cny(usd):
    # Convertir USD a CNY utilizando la tasa de conversión
    cny = usd * 6.75

    # Formatear el resultado con dos decimales y agregar 'Chinese Yuan'
    result = f"{cny:.2f} Chinese Yuan"

    return result


# Ejemplos de uso
print(usd_to_cny(15))  # Salida: '101.25 Chinese Yuan'
print(usd_to_cny(465))  # Salida: '3138.75 Chinese Yuan'
