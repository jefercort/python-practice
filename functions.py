# para crear una funcion se usa la palabra reservada def
# si por ejemplo no se envia un valor en alguno de los propiedades se puede asignar un valor por defecto
def holaKevin(name, lastName="No tiene apellido"):
    print("Hola grandioso y bendecido " + name + " " + lastName)

# para llamar la funcion se usa el nombre de la funcion seguido de parentesis
holaKevin("Kevin", "Cortes")
holaKevin("Sandra")

# Si no se pasan los parametros de manera organizada se puede hacer de la siguiente manera:
holaKevin(lastName="Cortes", name="Kevin")

# para retornar un valor se usa la palabra reservada return
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def calculadora():
    while True:
        print("Que operacion desea realizar?")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        option = int(input("Ingrese la opcion: "))

        if option == 5:
            print("Saliendo de la calculadora")
            break

        if option >= 1 and option <= 4:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))

            match option:
                case 1: print("La operacion tiene como resultado: ", suma(a, b)),
                case 2: print("La operacion tiene como resultado: ", resta(a, b)),
                case 3: print("La operacion tiene como resultado: ", multiplicacion(a, b)),
                case 4: print("La operacion tiene como resultado: ", division(a, b))
            
        else:
            print("Opcion no valida")
            continue
        
calculadora()