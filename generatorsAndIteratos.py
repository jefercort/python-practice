# Los iteradores van revisando cada elemento sin usar indices

# Ejemplo de iterador
myList = [1, 2, 3, 4, 5]
myIter = iter(myList)
# Usamos next para ir iterando en la lista y mostrar los elementos que se guardan en memoria
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
# Al llegar al final de la lista se genera un error
# print(next(myIter))

# Iterador de cadenas

myString = "Soy Kevin Cortes y SOY EL PUTO AMO"
myIterString = iter(myString)

for character in myIterString:
    print(character)


# Iterador para numeros impares (odd)

limit = 20

# oddNumbers = (i for i in range(1, limit) if i % 2 != 0)
oddNumbers = iter(range(1, limit + 1 , 2))

for number in oddNumbers:
    print(number)


# GENERADORES, PARA CREAR UNA FUNCION USAMOS LA PALABRA RESERVADA "def" Y PARA CREAR UN GENERADOR USAMOS LA PALABRA RESERVADA "yield"
# ya no se usa la palabra reservada return si no yield

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for number in myGenerator():
    print(number)

# Otro ejemplo es usando la serie de Fibonacci que es una serie de numeros donde cada numero es la suma de los dos anteriores
print("Serie de Fibonacci")
def fibonacci(limit):
    a, b = 0, 1
    # la linea anterior es igual a:
    # a = 0
    # b = 1
    while a < limit:
        yield a
        a, b = b, a + b

for number in fibonacci(1000):
    print(number)