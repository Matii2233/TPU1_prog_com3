# (1)

# arreglo abcdario para buscar las letras que formara nel mensaje encriptado
abcdario = "abcdefghijklmnñopqrstuvwxyz"
lugares = int(input("Cantidad de lugares de desplazamiento: "))

# ciclo para, que pide cinco mensajes y que limpia la variable cript para ser usada nuevamente
for i in range(5):
    mensaje = input("Escribe un mensaje: ")
    crypt = ""

    # recorremos el arreglo mensaje con un bucle para
    for letra in mensaje:
        # buscamos la posicion del arreglo "abcdario" que tenga el valor de "letra"
        if letra in abcdario:
            # variable "posicion" para guardar la posicion del arreglo "abcdario" encontrada
            posicion = abcdario.find(letra)
            posicion = (posicion+lugares)%27
            # variable "cript" para almacenar el nuevo mensaje encriptado
            crypt += abcdario[posicion]
        else:
            # si no se encuentra la posicion en el arreglo "abcdario" crypto acumula lo guardado en letra
            crypt += letra

    print("el mensaje ", i+1, " es ", crypt)




# (2)

print("puede ingresar numero enteros positivos hasta que ingrese el numero 0 y termine el programa")
num=int(input())
par=0
impar=0
tpar=0
timpar=0
import math


while num!=0:


    if num<0:
        print("el numero debe ser positivo.")
        num=0
    else:
        entero = num
        while entero>0:
            digit = num%10
            num = num/10
            entero = math.trunc(num)
            if digit%2==0:
                par+=1
                tpar+=1
            if digit%2 != 0:
                impar+=1
                timpar+=1
            if digit==0:
                par+=0
                tpar+=0
        print("el numero tenia ", par, "digitos pares y ", impar, " digitos impares")
        par=0
        impar=0
    

    num=int(input("ingrese un nuevo numero: "))


print("El total de los digitos pares fue de: ", tpar)
print("El total de los digitos impares fue de: ", timpar)
print("Saliendo...")
     