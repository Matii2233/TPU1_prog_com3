# 1- escribe un prpgrama que pida una palabra y la muestre en pantalla 10 veces

word = input("Escribe una palabra cualquiera: ")

for i in range(10):
    print("***",word, "***")




# 6- escribe un programa que pida al usuario un numero entero y muestre en pantalla un triangulo como el mostrado:
# *
# **
# ***
# ****

height = int(input("De un numero cualquiera: "))

for i in range(height):
    for j in range(i+1):
        print("*", end=" ")

    print("")




# 11- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra
#    introducida empezando por la última.

word = input("Escribe una palabra cualquiera: ")

for i in word:
    print(i," ", end="")




# 16- Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba
#    cuántos negativos ha introducido.

quantity=int(input("cuantos numeros se introduciran?: "))
neg_quantity=0


for i in range(quantity):
    print("numero ", i+1, ": ")
    numbers=int(input())

    if numbers<0:
        neg_quantity+=1


print("Hay un total de ", neg_quantity, " numeros negativos")




# 21- Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

number=int(input("Ingresa un numero cualquiera: "))
bigger_num = 0

if isinstance(number, float):
    print("El numero debe ser entero.")

elif number<1:
    print("el numero debe ser positivo")

elif isinstance(number, int):
    while number!=0:
        if number>bigger_num:
            bigger_num = number
            
        number = int(input("Ingresa un nuevo numero: "))

    print("De todos los numeros ingresados, el mayor fue: ", bigger_num)

