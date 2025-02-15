# la forma de representar una lista en python es con corchetes [] y los elementos separados por comas
# tambien se pueden incluir listas dentro de las listas (listas anidadas)
# las listas pueden contener cualquier tipo de dato
to_do = ["desayunar", "estudiar", "trabajar", "almorzar", "dormir", ["jugar", "ver tv"]]
# to_do = ["desayunar", "estudiar", "trabajar", "almorzar", "dormir"]
print(type(to_do))

# para saber cuantos elementos tiene una lista se usa la funcion len()
print(len(to_do))

# para acceder a un elemento de la lista se usa el indice
print(to_do[5])

# para hacer slicing se usa la notacion [inicio:fin] donde inicio es el indice donde se inicia y fin es el indice donde se termina
print(to_do[1:4])
# si quiero ir desde la posicion 1 hasta el final de la lista se puede hacer de la siguiente manera
print(to_do[1:])
# si quiero ir desde el inicio de la lista hasta la posicion 4 se puede hacer de la siguiente manera
print(to_do[:4])

# para modificar un elemento de la lista se usa el indice
to_do[0] = "desayunar y estudiar"

# para agregar un elemento a la lista se usa el metodo append()
to_do.append("hacer ejercicio")

# para agregar varios elementos a la lista se usa el metodo extend()
to_do.extend(["leer", "escuchar musica"])
print(to_do)

# para insertar un elemento en una posicion especifica se usa el metodo insert()
to_do.insert(3, "tomar cafe")
print(to_do)

# para eliminar un elemento de la lista se usa el metodo remove()
to_do.remove("tomar cafe")

# para eliminar un elemento de la lista por su indice se usa el metodo pop()
to_do.pop(3)

# para eliminar todos los elementos de la lista se usa el metodo clear()
to_do.clear()

# para eliminar la lista se usa la palabra reservada del
del to_do

# para copiar una lista se puede hacer de la siguiente manera

to_do = ["desayunar", "estudiar", "trabajar", "almorzar", "dormir", ["jugar", "ver tv"]]
to_do_copy = to_do.copy()
print(to_do_copy)

# tambien se puede hacer de la siguiente manera
to_do_copy = list(to_do)
print(to_do_copy)

# para concatenar listas se usa el operador +
to_do_1 = ["desayunar", "estudiar", "trabajar"]
to_do_2 = ["almorzar", "dormir"]
to_do = to_do_1 + to_do_2
print(to_do)

# para buscar un elemento en la lista cuando aparece por primer vez se usa el metodo index()
print(to_do.index("almorzar"))

# En una lista de numeros si quiero saber cual es el mayor y el menor se puede hacer de la siguiente manera
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print(max(numbers))
print(min(numbers))
