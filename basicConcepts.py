saludo = "    hello"
nombre = "Kevin"
age = 32

print("I am overachiever")
print("Yes, you are "  + nombre + " i am " + str(age) + " years old")

# PARA SABER QUE TIPO DE DATO ES UNA VARIABLE USO type()

print(type(saludo))
print(type(age))

# SE PUEDEN USAR COMILLAS SIMPLES TRIPLES SI SE QUIERE BAJAR DE ESPACIO O TENER ALGO DIFERENTE PARA VISUALIZAR

saludo_2 = '''Hello

my name is Kevin 

and i Am a Overachiever'''

print(saludo_2)

# PARA SABER LA POSICION DE ALGUN CARACTER EN LA CADENA USAMOS [] Y EL NUMERO DE LA POSICION 
# TAMBIEN SE PUEDE USAR NEGATIVOS PARA EMPEZAR DESDE EL FINAL

print(saludo_2[18])
print(saludo_2[-12])

# PARA SABER LA LONGITUD DE UNA CADENA USAMOS len()

print(len(saludo_2))

# PARA SABER SI UNA PALABRA ESTA EN UNA CADENA USAMOS in

print("Kevin" in saludo_2)

# PARA SABER CUANTAS VECES SE REPITE UNA PALABRA EN UNA CADENA USAMOS count()

print(saludo_2.count("Kevin"))

# PARA REPLICAR UNA CADENA USAMOS EL OPERADOR DE MULTIPLICACION

print(saludo_2 * 2)

# LOS METODOS PARA PONER EN LOWER O UPPER UNA CADENA SON lower() Y upper()

print(saludo_2.lower())
print(saludo_2.upper())

# SI QUIERO ELIMINAR LOS ESPACIOS DEL INICIO Y DEL FINAL USAMOS .strip()

print(saludo.strip())

