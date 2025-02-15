# Para especificar el uso de diccionarios usamos {} y separamos los elementos con comas.

numbers = {1: "one", 2: "two", 3: "three"} # Creación de un diccionario

print(numbers[1]) # Acceso a un elemento del diccionario por medio de la key

user = {"name": "John", "age": 30} # Creación de un diccionario
print(user["name"]) # Acceso a un elemento del diccionario por medio de la key
print(user) # Imprimir el diccionario completo

del user["age"] # Eliminar un elemento del diccionario

print(user) # Imprimir el diccionario completo

# para saber las llaves o keys de un diccionaro usamos el método keys()

print(numbers.keys()) # Imprimir las keys del diccionario

# para saber los valores de un diccionario usamos el método values()
print(numbers.values()) # Imprimir los valores del diccionario

users = {
    "1010206717":
    {"name": "Kevin",
     "last_name": "Smith",
     "age": 32,
     "height": 1.80,
     "nacionality": "USA"},
     "1015426375":
     {"name": "Sandra",
     "last_name": "Noniote",
     "age": 33,
     "height": 1.60,
     "nacionality": "CUERPO RICO"}
}

print(users["1010206717"])