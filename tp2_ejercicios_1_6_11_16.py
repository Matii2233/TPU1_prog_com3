# (1) Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola
#     que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años

print ("ingrese los años de antiguedad de su computadora: ")
años = int(input())
print("")


if años<=2:
    print("El computador es nuevo")
elif años>2:
    print("El computador es viejo")




# (6) Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto 
#     debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

print("ingrese un año")
año = int(input())


if (año<100):
    if (año%4==0):
        print("el año ", año, " es bisiesto")
    else:
        print("El año ", año, " no es bisiesto")
elif (año>99 and año<400):
    if (año%4==0) and (año%100!=0):
        print("el año ", año, " es bisiesto")
    else:
        print("el año ", año, " no es bisiesto")
elif (año>399):
    if (año%4==0 and año%100!=0) or (año%4==0 and año%400==0):
        print("el año ", año, " es bisiesto")
    else:
        print("el año ", año, " no es bisiesto")

    


# (11) La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza
#      aparecen a continuación.

#          -Ingredientes vegetarianos: Pimiento y tofu.
#          -Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón.
#
#      Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta
#      le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella 
#      y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no 
#      y todos los ingredientes que lleva.

vegetariano = False


print("BIENVENIDO a la toma de pedido de la pizzeria *Bella Napoli")
print("A continuacion, indique si prefiere un menu vegetariano o no vegetariano...")
input("(si) para menu vegetariano. (no) para menu NO vegetariano")
vegetariano = input()
print("Todas las pizzas llevan tomate y mozzarella. A continuacion elija los ingredientes extra: ")


if (vegetariano == True):
    print("Escriba el ingrediente seguido de una coma, un espacio y el siguiente ingrediente asi: ")
    print("ingrediente, ingrediente, ingrediente")
    print("ingredientes vegetarianos: ")
    print(" ")
    print(" -Pimiento")
    print(" -Tofu")
    ingredientes = input()
elif (vegetariano == False):
    print("Escriba el ingrediente seguido de una coma, un espacio y el siguiente ingrediente asi: ")
    print("ingrediente, ingrediente, ingrediente")
    print("ingredientes no vegetarianos: ")
    print("")
    print(" -Pepperoni")
    print(" -Jamon")
    print(" -Salmon")
    ingredientes = input()


if vegetariano == True:
    print("Pizza vegetariana. Ingredientes: ")
    print(ingredientes)




# (16) Haz una calculadora básica pida al usuario dos valores, a y b. Según la opción que desean, realizar la operación: 
#        - Si operación es 1 entonces debemos ver el resultado de a + b
#        - Si operación es 2 entonces debemos ver el resultado de a * b
#        - Si operación es 3 entonces debemos ver el resultado de a - b
#        - Si operación es 4 entonces debemos ver el resultado de a / b

print("Ingrese dos valores")
a = int(input())
b = int(input())


print("Elija que operacion realizara entre suma, resta, multiplicacion y division.")
print("Al restar, se hara (a-b), y al dividir se hara (a/b)")
print("escibir el nombre de una de ellas sin comas ni espacios ni mayusculas: ")
op = input()

if op == "suma":
    resultado = a+b
    print("el resultado es: ", resultado)


if op == "resta":
    resultado = a-b
    print("el resultado es: ", resultado)


if op == "multiplicacion":
    resultado = a*b
    print("el resultado es: ", resultado)


if op == "division":
    resultado = a/b 
    print("el resultado es: ", resultado)