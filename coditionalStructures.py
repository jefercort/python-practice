x = 10 

if x > 5: 
    print("x es mayor que 5")
elif x < 5:
    print("x es menor que 5")
else:
    print("x es igual a 10")

y = 5

if x > 5 and y > 5:
    print("x y y son mayores que 5")

if x > 5 or y > 5:
    print("x o y son mayores que 5")

#para realizar una negacion
if not x > 5:
    print("x no es mayor que 5")


isMember = True
age = 22

if isMember:
    if age >= 18:
        print("Puede ingresar al club")
    else:
        print("No puede ingresar al club")
else:
    print("No puede ingresar al club")