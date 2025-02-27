# Esta es como en JavaScript se usa el try:catch para manejar lo errores en Python se usa el try:except. 
# En el siguiente ejemplo se muestra como se puede usar el try:except para manejar errores en Python.

try:
    divisor = int(input("Ingrese el divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("Solo se permiten numeros")
except Exception as e:
    print("Error desconocido: ", e)


# en esta funcion podemos ver todas las expceciones de python
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

print_exception_hierarchy(Exception)