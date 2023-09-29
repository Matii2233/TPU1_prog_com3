import random

def ahorcado(userword,lifes):
    while lifes>0:
        #hay un contador de fallos por si el usuario adivina la palabra sin cometer fallos
        fails=0

        print("Ingresa una letra para adivinar la palabra:")
        for letter in word:
            if letter in userword:
                print(letter,end="")
            else:
                print("_",end="")
                fails+=1
            
            #como dijimos antes, si no se cometen fallos, se da un mensaje de victoria y se da un break
            if fails==0:
                print("!!! Felicidades, Ganaste¡¡¡")
                break

        #Ingreso de la letra por el usuario y se acumula en la variable palabra del usuario
        print()
        userletter=input(">")
        userword+=userletter

        #se restan vidas cuando la letra ingresada no se encuentra en la palabra tomada de la lista
        if userletter not in word:
            lifes-=1
            print("Letra equivocada :(")
            print("Te quedan",lifes,"vidas")

        #cuando vidas llega a 0 se envia un mensaje y al volver a la condicion del while, se sale del cilo.
        if lifes==0:
            print()
            print("Lo siento. Has perdido")
    else:
        #cuando se sale del ciclo se envia un mensaje
        print("Gracias por participar")




#Se inicia pidiendo el nombre y creando una lista de palabras
print("¿Cual es tu nombre?")
name=input(": ")
print("hola",name,". Vamos a jugar al ahorcado X-)")
print()

wordslist=["laringe","epiglotis","vibrato","falsete","distoricion","agudo","grave","medio","melisma","afinacion"]
#se elige una palabra al azar y se guarda en una avriable
word=random.choice(wordslist)
#tambien se crea una variable para acumular las letras que ingresara el usuario
userword=""
#yp por ultimo un contador de vidas
lifes=5

#se entra en la funcion del ahorcado
ahorcado(userword,lifes)