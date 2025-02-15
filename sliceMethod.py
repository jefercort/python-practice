# al momento de copiar una lista no solo se copia la lista si no tambien su espacio en memoria
# es decir si se modifica la copia tambien se modifica la lista original
# para evitar esto se puede hacer una copia de la lista con el metodo slice
# listaCopia = listaOriginal[:]
# o
# listaCopia = listaOriginal.copy()
# o
# listaCopia = list(listaOriginal)

listaOriginal = [1, 2, 3, 4, 5]
listaCopia = listaOriginal[:]
listaCopia[0] = 100
print(listaOriginal)
# el metodo id lo usamos para ver la direccion de memoria de la lista original y la copia
print(id(listaOriginal))
print(id(listaCopia))
