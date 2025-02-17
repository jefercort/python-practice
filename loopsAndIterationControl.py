numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    print(i)

# Para iterar en un rango especicifo se hace lo siguiente:
for i in range(1, 11):
    print(i)

# Para iterar en un rango especifico con un salto de 2 se hace lo siguiente:
for i in range(1, 11, 2):
    print(i)

toys = ["car", "ball", "doll", "puzzle"]

for toy in toys:
    if toy == "doll":
        print("I found the doll")
        continue

# Para usar while se hace lo siguiente:
y = 22

while y > 0:
    print(y)
    if y == 10:
        break
    y -= 1