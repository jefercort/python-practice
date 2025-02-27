# La recursividad es un concepto muy importante en programación y se refiere a la capacidad de una función de llamarse a sí misma. 
# En Python, una función puede llamarse a sí misma si se cumplen ciertas condiciones. 
# La recursividad es una técnica poderosa que se utiliza en muchos algoritmos y problemas de programación.

# Ejemplo para factoriales
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(100))

# Ejemplo para la serie de Fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))

# Ejemplo de recursividad para la sumatoria de numeros naturales

def suma_natural(n):

    # Calcula la sumatoria de números naturales hasta n usando recursividad.
    
    # :param n: Número natural hasta el cual se quiere calcular la sumatoria.
    # :return: Sumatoria de los números naturales desde 1 hasta n.

    if n <= 0:
        return 0  # Caso base: si n es 0 o negativo, la suma es 0
    return n + suma_natural(n - 1)  # Llamado recursivo

num = int(input("Ingrese un número natural: "))
resultado = suma_natural(num)
print(f"La sumatoria de los números naturales hasta {num} es: {resultado}")
