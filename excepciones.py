"""
1. Escribe un programa que intente dividir dos números. Si el segundo número 
es cero, captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
"""
def division(a,b):
    try:
        resultado = a / b
        print(f"El resultado de la división es: {resultado}")
    except ZeroDivisionError as e: # except Exception as e... es válido también
        print(f"Error: {e}. No es posible dividir por 0")

division(10,2)


"""
2. Escribe un programa que intente sumar un número y una cadena. Si se produce 
un error de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
"""
def numero_cadena():
    try:
        10 / "5"
    except TypeError as e:
        print(f"Error: {e}. No es posible sumar string con int.")

numero_cadena()


"""
3. Escribe un programa que intente acceder a una clave que no existe en un diccionario. 
Si se produce una excepción KeyError, captura la excepción y muestra.
"""

diccionario = {"nombre":"Tomás", "apellido":"Perez"}

def acceder_diccionario():
    diccionario = {"nombre":"Tomás", "apellido":"Perez"}

    try:
        key = diccionario["estado_civil"]
        print(f"Clave: {key}")
    except KeyError as e:
        print(f"La clave {e} no existe en el diccionario.")

acceder_diccionario()

"""
4. Escribe un programa que intente abrir un archivo que no existe. Si se produce 
una excepción FileNotFoundError, captura la excepción y muestra un mensaje de error 
al usuario. Sin embargo, también intenta crear el archivo si no existe.
"""
try:
    with open('ejercicio_5.txt','r',encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)

except FileNotFoundError as e:
    print(f"Error: {e}. El archivo no existe.")
    print("Creando archivo")

    # Creando el archivo (modo escritura)
    with open('ejercicio_5.txt','w', encoding="utf-8") as archivo:
        archivo.write("Archivo que forma parte de un ejercicio de manejo de excepciones.")
    print("Archivo creado.")


"""
5. Escribe un programa que intente dividir dos números. Si el segundo número es cero, 
captura la excepción ZeroDivisionError. Si el primer número es un número no válido, 
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
"""

def dividir():
    try:
        numero1 = float(input("Ingrese primer número: "))
        numero2 = float(input("Ingrese segundo número: "))
        resultado = numero1 / numero2
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except ValueError:
        print("Error: el primer número ingresado no es válido")

dividir()
