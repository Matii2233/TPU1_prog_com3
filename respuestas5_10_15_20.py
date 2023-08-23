# (5) ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

#     a) A = input(nombre, “¿Cuál es tu canción favorita?”)
#        El problema es que se quisieron concatenar dos elementos dentro del input
#        Para solucionarlo se puede poner asi:

nombre = "Matias"
print(nombre, "¿cual es tu cancion favorita?")
a = input()


#     b) precio = input(“Precio: “)
#        total = precio + (precio * 0.1)
#        en este ejemplo, "precio" esta guardanto una cadena de texto y luego se esta quieriendo multiplicar
#        lo correcto seria lo siguiente:


precio = int(input("Precio: "))
total = precio + (precio*0.1)
print(total)


#     c) edad = int(input(“Edad: “))
#        print(tu edad es, edad)
#        El problema es que a ldevolver un texto no se usaron comillas. 
#        La solucion seria hacerlo asi:


edad = int(input("Edad: "))
print("tu edad es", edad)


#     d) edad = int(input(“Edad: “))
#        print(“Veamos si tu edad es 18…”, edad=18)
#        El problema del ejemplo es que se estaba asignando el valor "18" a una variable dentro de un print()
#        lo correcto, para comprobar si "edad" es igual a "18", seria lo siguiente:


edad = int(input("Edad: "))
print("Veamos si tu edad es 18…")


if edad==18:
    print("Tu edad es 18")
else:
    print("Tu edad no es 18")




# (10) Un alumno desea saber cual será su calificación final en la materia de Algoritmos.
#      Dicha calificación se compone de los siguientes porcentajes:
        
#        - 55% del promedio de sus tres calificaciones parciales.
#        - 30% de la calificación del examen final.
#        - 15% de la calificación de un trabajo final.


p1 = 80
p2 = 60
p3 = 90
prm_parciales = (p1+p2+p3)/3
efinal = 80
tfinal = 90


nota_final = (prm_parciales*0.55) + (efinal*0.30) + (tfinal*0.15)
print("La nota final de algoritmos es: ", nota_final)




# (15) Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
#      Escribir un algoritmo que determine la hora de llegada a la ciudad B.


hh = 15
mm = 30
ss = 0
t = 1800
ss = ss + t


if ss>59:
    mm = mm + ss/60
    ss = 0

if mm>59:
    hh = hh + mm/60
    mm = 0

if hh>24:
    hh = 0


print("La hora de llegada a la ciudad B sera las: ", hh, ":", mm, ":", ss)




# (20) Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DD MM AAAA.


fecha = [ int(input("Dia de nacimiento: ")), int(input("Mes de nacimiento: ")), int(input("Año de nacimiento: ")) ]
print("su fehca de cumpleaños es el: ", fecha)