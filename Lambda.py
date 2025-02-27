# La funcion Lambda es una funcion anonima que se puede usar para realizar operaciones sencillas y que no requieran de mucho codigo. 
# A continuacion se muestra un ejemplo de como se puede usar la funcion Lambda para realizar la suma de dos numeros:

suma = lambda a, b: a + b
print(suma(5, 5))

# En este caso se esta creando una funcion llamada suma que recibe dos parametros a y b y retorna la suma de estos dos numeros.

multiplicacion = lambda a, b: a * b
print(multiplicacion(5, 5))

# Cuando estamos utilizando listas y queremos aplicar la funcion a cada uno de ellos usamos .map() y la funcion lambda. 
# A continuacion se muestra un ejemplo de como se puede usar la funcion lambda con .map():

numbers = range(11)
# tengo una lista donde se va almacenando lo que vamos aplicar con map
squared = list(map(lambda x: x ** 2, numbers))
print("Cuadrados de numeros: ", squared)

# Si estamos buscando una condicion especficia en una lista podemos usar la funcion lambda con .filter().
# Vamos a sacar los numeros pares de numbers

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Numeros pares: ", even)

# Ahora vamos a sacar los numeros impares de numbers

odd = list(filter(lambda x: x % 2 != 0, numbers))
print("Numeros impares: ", odd)
