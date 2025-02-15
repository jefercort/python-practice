# para crear y usar las comprehensionLists se hace lo siguiente:

squares = [x**2 for x in range(1, 10)]
print(squares)

# se puede agregar una condicion para filtrar los elementos
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(even_squares)

# se puede hacer una lista de listas
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

# Ejemplo de temperatura

celcius = [0, 10, 20, 30, 40]
fahrenheit = [(9/5)*temp + 32 for temp in celcius]
print(fahrenheit)


# Ejemplo para hacer la transpuesta de una matriz
matrix_1 = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

transpose = [[row[i] for row in matrix_1] for i in range(len(matrix_1[0]))]

print(matrix_1)
print(transpose)

# Ejemplo haciendolo con varias lineas de codigo es lo mismo que se hizo con el comprehensionList

matrix_2 = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

transpose_2 = []
for i in range(len(matrix_2[0])):
    transposed_row = []
    for row in matrix_2:
        transposed_row.append(row[i])
    transpose_2.append(transposed_row)

print("MATRIZ 2", transpose_2)