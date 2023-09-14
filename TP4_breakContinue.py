# =================================================== PUNTO 1.1 ===================================================
# Crear un bucle while con las especificaciones dadas:

x=0

while x<30:
    x+=1

    if x==4 or x==6 or x==10:
        print("El valor ", x, " de x fue omitido")
        continue

    if x==15:
        print("La ejecucion del bucle se rompio cuando x tomo el valor ", x)
        break

    print(x)




# =================================================== PUNTO 1.2 ===================================================

# Programa que permita ingresar lineas de texto secuencialemtne, mostrando una conversion a mayusculas
# de las lineas. Finalmente que termine el programa al ingresar una linea vacia




times=int(input("¿Cuantas veces ingresara una linea de texto?: "))
print("Deja la linea en blanco para terminar (sin espacios)")
print("ingresa una linea de texto:")

for i in range(times):
    textline=input(": ")

    if textline=="":
        #Realiza un break cuando se ingresa una linea en blanco
        print("Se dejo la linea en blanco. Saliendo...")
        break
    print("   >",str.upper(textline))




# =================================================== PUNTO 2 ===================================================

# Programa que administre una cuenta bancaria usando la bitacora. Que al ingresar un espacio vacio
# termine el programa y muestre en la salida el resultado de los movimientos




funds=1500
entry=0
withdrawl=0
action=0
print("")
print("Los fondos son: ",funds," pesos")
print("Para salir debe ingresar o retirar un valor vacio (enter vacio)")

while funds>=0:
    # En este if, en la parte verdadera (fondos==0) esta el programa sin la funcion de retirar dinero
    # y en la parte falsa (funds!=0) esta el mismo codigo pero con la funcion retirar dinero. 
    if funds==0:
        print("")
        print("Tiene fondos = 0. Retiro de dinero imposibilitado.")
        print("")
        print("1.  dejar")
        print("")
        action=int(input())

        #verifica que se ingrese un numero correspondiente con una opcion
        if action>2 or action<0:
            print("")
            print("numero ingresado no correspondiente. Saliendo...")
            break
        if action==1:
            entry=input(": ")

            #conodicion de salida
            if entry=="":
                print("")
                print("Saliendo...")
                break
            funds=funds+int(entry)
    else:
        print("")
        print("1.  dejar")
        print("2.  retirar")
        print("")
        action=int(input())

        if action>2 or action<0:
            print("")
            print("numero ingresado no correspondiente. Saliendo...")
            break
        if action==1:
            entry=input(": ")

            #condicion de salida
            if entry=="":
                print("")
                print("Saliendo...")
                break
            funds=funds+int(entry)
        if action==2:
            withdrawl=input(": ")

            if withdrawl=="":
                print("")
                print("Saliendo...")
                break
            # Si se intenta retirar mas dinero del que hay, se envia un mensaje y se da un continue
            if int(withdrawl)>funds:
                print("")
                print("Los fondos son insuficientes")
                continue
            funds=funds-int(withdrawl)
print("Fondos: ",funds)




# =================================================== PUNTO 3 ===================================================

# Programa que admita numeros mayores que 1 para mostrar cuantos numero primos se ingresaron. El programa
# terminara cuando se ingrese el cero




nums=2
primenums=0
dividers=0

while nums>1:
    print("")
    print("Ingrese un numero mayor que 1, o ingrese 0 para salir:")
    nums=int(input())

    #Ifs para evitar que se ingrese el numero 1 o numeros negativos
    if nums==0:
        break
    if nums<0:
        print("")
        print("ERROR. El numero no puede ser negativo")
        continue
    if nums==1:
        print("")
        print("ERROR. El numero debe ser mayor que 1")
        continue
    if nums>0:
        #bucle for que cuenta los divisores del numero ingresado para saber si este es primo
        for i in range(nums):
            if nums%(i+1)==0:
                dividers+=1

        if dividers==2:
            primenums+=1

        dividers=0
print("")
print("Se ingresaron un total de ",primenums," numero primos")
print("Saliendo...")




# =================================================== PUNTO 4 ===================================================

# Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango.
#  que sean bisiestos y múltiplos de 10. 

print("ingrese desde el año: ")
fromyear = int(input())
print("hasta el año: ")
toyear = int(input())

for i in range(fromyear, toyear):
    if toyear<=fromyear:
        print("")
        print("El segundo año debe ser mayor al primero. Saliendo...")
        break
    if toyear<0:
        print("")
        print("El primero año no puede ser un numero negativo. Saliendo...")
        break
    if i%4==0 and i%100!=0 or i%400==0:
        print("El año ",i," es biciesto")
    if i%10==0:
        print("El año ",i," es multiplo de 10")




# =================================================== PUNTO 5 ===================================================

# Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. 
# Utiliza la declaración continue para omitir los números impares.

print("")
for i in range(20):
    if i%2!=0:
        continue
    else:
        if i==18:
            print(i+2, end="")
        else:
            print(i+2,", ", end="")




# =================================================== PUNTO 6 ===================================================

# Crea una lista de números y utiliza un bucle for para encontrar un número específico. cuando encuentres
# un numero, usa un break para salir del bucle

data = (0,1,2,3,5,8,13,21,34,55)
element = 13

print("")
print("El numero buscado es: ",element)

for i in data:
    if element in data:
        print("")
        print("El numero",element,"fue en contrado en la posicion",data.index(element),"dentro de la siguiente lista:")
        print(data)
        print("")
        print("Saliendo...")
        break




# =================================================== PUNTO 7 ===================================================

action=1

while action<4 and action>0:
    print("")
    print("1.  mostrar mensaje 1")
    print("2.  mostrar mensaje 2")
    print("3.  mostrar mensaje 3")
    print("0.  salir")
    print("")
    action = int(input())
    print("")

    # If que valide que se introdujo un numero valido
    if action<0 or action>3:
        print("")
        print("El numero ingresado no corresponde con una opcion disponible.")
        continue
    if action==0:
        print("")
        print("Saliendo...")
    if action==1:
        print("")
        print("Elijio la opcion 1. BUENOS DIAS")
    if action==2:
        print("")
        print("Elijio la opcion 2. BUENAS TARDES")
    if action==3:
        print("")
        print("Elijio la opcion 3. BUENAS NOCHES")