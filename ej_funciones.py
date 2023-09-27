# HAY QUE CORREGIR EL NOMBRE DE LAS VARIABLES DENTRO DE LAS FUNCIONES. ESTAS DEBEN TENER EL
# MISMO NOMBRE QUE LOS ARGUMENTOS DE LA FUNCION

#funcion
#most
def most(a,b):
    if a>b:
        return a
    else:
        return b
    
#leats

def least(a,b):
    if a<b:
        return a
    else:
        return b
    



#programa principal
x = int(input("Numero 1: "))
y = int(input("Numero 2: "))

print(most(x-3, least(x+2, y-5)))