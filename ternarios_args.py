"""
Calcular el mayor de dos números ingresados por teclado usando un operador ternario.
"""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

numero_mayor = a if a > b else b
print(f"El {numero_mayor} es el número mayor.")

"""
Buscar una palabra en una lista ingresada por teclado usando args y un operador ternario.
"""

def buscar_palabra(*args):
    palabra = input("Ingrese la palabra que quiera buscar: ").strip()
    resultado = f"Se encontró exitosamente la palabra '{palabra}'." if palabra in args else f"No se encontró la palabra '{palabra}'."
    print(resultado)

lista = input("Ingrese las palabras (separadas por coma): ").strip().split(",")

buscar_palabra(*lista) # Desempaquetado de la lista como args


"""
Determinar si un número es par o impar.
"""
numero = int(input("Ingrese un número: "))
print(f"{numero} es par." if numero % 2 == 0 else f"{numero} es impar.")


"""
Calcular el promedio de una lista de números usando args y un operador ternario.
"""

def promedio(*args):
    calculo_prom = sum(args) / len(args) if len(args) > 0 else "No es posible calcular el promedio sin datos!"
    print(f"Promedio: {calculo_prom}")

numeros_input = input("Ingrese los números separados por comas: ").strip() 

# Convierte el input del user en lista de floats
numeros_lista = [float(num) for num in numeros_input.replace(",", " ").split() if num]

promedio(*numeros_lista) # Desempaquetado de la lista