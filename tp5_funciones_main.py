from funciones import *

'''

#******************************************************************* PUNTO 1 *******************************************************************
# Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.


print("D.N.I: ")
dni = int(input())

# se llama a la funcion que retorna true or false
print(validation(dni))





#******************************************************************* PUNTO 2 *******************************************************************
# Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.
#funcion que divide la cadena en una lista de palabras y devueve la longitud de la ultima palabra


print("Ingrese una cadena de caracteres o una palabra")
text=input(">")
print()

print("La longitud de la ultima palabra del texto es de",last_word_lenght(text),"caracteres")




#*******************************************************************PUNTO 3*******************************************************************
# Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club.
# Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.


print("Ingrese los datos de los socios:")
print("cuando ingrese un nombre vacio, se dara por terminado el procesamiento")
print()
fullname="a"
dni=""
while fullname:
    print("Ingrese el dni y el nombre completo")
    print("Se finalizara cuando ingrese un nombre vacio")
    print()
    dni = input("DNI: ")
    print()
    fullname = input("nombre completo: ")


    if fullname == "":
        print("saliendo...")
        break
    

    #solo si se cumple que dni tiene de 7 a 8 caracteres, se llama a la funcion
    if len(dni)>=7 and len(dni)<=8:
        print("el/la socio/a:",fullname)
        print("DNI:",dni)
        print()
        #llamado a la FUNCION
        print("Tiene el ID de socio:",id_obtaining(fullname,dni))
    else:
        #si no se cumple, se entra en un ciclo que pide el dni, hasta que este tenga de 7 a 8 caracteres
        #luego se llama a la funcion
        print("el dni debe tener de 7 a 8 caracteres")
        while len(dni)<7 or len(dni)>8:
            dni=input("DNI: ")

        print("el/la socio/a:",fullname)
        print("DNI:",dni)
        print()
        print("Tiene el ID de socio: ")
        #llamado a la FUNCION
        print(id_obtaining(fullname,dni))




#*******************************************************************PUNTO 4*******************************************************************
#Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.


print("Ingrese dos numeros para saber si uno es multiplo del otro")

number1 = int(input("Numero1: "))
number2 = int(input("Numero2: "))

if is_mult(number1,number2):
    print("Al menos uno de numeros es multiplo del otro")

if the_first_is_mult(number1, number2):
    print("El primer numero es multiplo del segundo")




#*******************************************************************PUNTO 5*******************************************************************

#Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
#Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media.
#El programa pedirá el número de días que se van a introducir.


print("Ingrese la cantidad de dias de los que desea obtener la temperatura media")
days=int(input("> "))
countdown=0

print()
print("Ingrese la temperatura maxima y luego la minima, o la minima y luego la maxima:")
print()
while countdown < days:
    print()
    temp1 = int(input("  Temperatura 1: "))
    temp2 = int(input("  Temperatura 2: "))

    print()
    print("La temperatura media del dia es de",temp_average(temp1,temp2),"grados")
    countdown+=1




#*******************************************************************PUNTO 6*******************************************************************
#Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. 
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

        
#main
obtainedtext=""
print("Ingresa un texto cualquiera:")
text=input("> ")

#llamada a la funcion
print("tu texto:",text)
print("Texto resultante:",text_modifier(text,obtainedtext))




#*******************************************************************PUNTO 7*******************************************************************
#Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
#Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.


print("Ingresa 5 valores de una nueva lista: ")
nums_list=[]
i=0
while i<5:
    print("valor",i+1)
    nums_list.append(int(input("> ")))
    i+=1

print("Su nueva lista es:")
for num in nums_list :
    print(num,"",end="")
print()

min, max = obtain_max_and_min(nums_list)




#*******************************************************************PUNTO 8*******************************************************************
#Crear una funcion que reciba el radio de una circunferencia y devuelva el area y perimetro de la misma.
#Luego elaborar un programa que ingrese el radio de la circunferencia y utilice la funcion para obtener el area y perimetro.


print("Ingrese el radio de una circunferencia:")
radius=float(input("> "))
area,perimeter = obt_area_perimeter(radius)
print()

print("El area de la circunferencia es ",area," y el perimetro es ",perimeter)




#******************************************************************PUNTO 9*******************************************************************
#Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
#Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.


tries = 0
while tries < 3:
    username = input("username: ")
    password = input("password: ")
    access,tries = login(username,password,tries)

    if access == True:
        print()
        print("Iniciando sesion...")
        break

    print()
    print("Nombre de usuario o contraseña incorrecta. te quedan",3-tries,"intentos")




#******************************************************************PUNTO 10******************************************************************
# Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y porcentajes
# del carrito de compra,  aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.


costs = { "cost1":2200  ,  "cost2":5000  ,  "cost3":4700  ,  "discount1":0.05  ,  "discount2":0.1  ,  "discount3":0.15 }
print("El precio total de la compra es de ",apply_discount(costs)," pesos")




#*******************************************************************PUNTO 11*****************************************************************
# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado 
# de aplicar la función dada a cada uno de los elementos de la lista.


nums = [5,-123,83,8,-5.-10,0,7]
print("lista de numeros: ")
print(nums)
print()

print("los valores absolutos de la lista son: ")
print(apply_absolute_value(nums))




#*******************************************************************PUNTO 12*****************************************************************
#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.


print()
text="hola buen dia lleno por favor"
print("La frase es: '" +text+ "'")
print()
words_dictionary,dictionary_lenght = text_to_dictionary(text)

print("El diccionario que contiene las palabras de la frase es:")
print(words_dictionary)
print()
print("La longitud del diccionario llego a:")
print(dictionary_lenght)
print()




#*******************************************************************PUNTO 13*****************************************************************
#Escribir una función que calcule el módulo de un vector.


nums=[1,4,1,5,9,2,6,5]
print("De la lista ")
print(nums)
print()
print("Obtenemos los modulos de de la lista anterior dividida entre dos:")
print(get_module(nums))




#*******************************************************************PUNTO 14*****************************************************************
# Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.
         

print("ingresa un numero entero:")
num = int(input("> "))
print()

if prime_nums(num):
    print("El numero es primo")
else:
    print("El numero no es primo")




#*******************************************************************PUNTO 15*****************************************************************

# Escribir un programa que pida números al usuario, motrar el factorial de cada uno y,
# al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.


acumulator=0
while exit!=0:
    num, acumulator = input_nums(acumulator)

    print("El factorial del numero es:")
    print(get_factorial(num))
    print()
    print("ingrese 0 para salir. O cualquier otro numero par continuear")
    exit=int(input())

print("El total de numeros ingresados fue: ",acumulator)




#*******************************************************************PUNTO 16*****************************************************************

# Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, 
# utilizando para ello una función que calcule la frecuencia.


print("Ingresa un digito:")
digit=int(input())
print()
digit_lenght = len(str(digit))

if digit_lenght>1:
    print("Se debe ungresar UN SOLO digito")

    while digit_lenght>1:
        print("Ingresa otro digito:")
        digit=int(input())
        digit_lenght = len(str(digit))
        print()

print("Ingresa un numero:")
num=int(input())
print()

print("La cantidad de ocurrencias del digito en el numero es:")
print(get_currencys(num, digit))




#*******************************************************************PUNTO 17*****************************************************************
# Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo.
# Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.


largestnum=0
print()
print("Ingresa numeros primos. Ingresa un numero no primo para salir.")
print()
num = int(input("> "))
print()

prime=prime_nums(nums)

if num>largestnum:
    largestnum=num

print()
print("Ingresa un digito:")
digit=int(input())
print()
digit_lenght = len(str(digit))

digit, digit_lenght=digit_validation(digit,digit_lenght)

while prime==True:
    print("la suma de los digitos del numero es ",show_digits_sum(num))
    print()
    print("La ocurrencia del digito en el numero es de ",get_currencys(num,digit))
    print()
    print("=========================================================================")
    print()
    num = int(input("> "))
    print()
    
    if num<=1:
        prime=False
        print("saliendo...")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime=False
                print("saliendo...")
            else:
                prime=True
            
    if num>largestnum:
        largestnum=num

    print()
    print("Ingresa un digito:")
    digit=int(input())
    print()
    digit_lenght = len(str(digit))

    if digit_lenght>1:
        print("Se debe ungresar UN SOLO digito")
        print()
        
        while digit_lenght>1:
            print("Ingresa otro digito:")
            digit=int(input())
            digit_lenght = len(str(digit))
            print()

print("la suma de los digitos del numero es ",get_factorial(largestnum))

'''