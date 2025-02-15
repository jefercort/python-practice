nombre = input("Cual es tu nombre? ")
print("Hola", nombre)
age = input("Cual es tu edad? ")
print("Tu edad es", age)

# Para que los numeros sean numeros y no strings, se debe hacer un casting a int o float

age = int(input("Cual es tu edad? ")) # Se convierte a entero
# o para que sea float
age = float(input("Cual es tu edad? ")) # Se convierte a flotante
print(type(age))