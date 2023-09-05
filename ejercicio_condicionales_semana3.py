# variables booleanas para saber que dia de la semana es del lunes al viernes
vv = False
vv2 = False
vv3 = False
vv4 = False
vv5 = False

# variables para calcular el porcentaje de aprobados de los niveles inicial, intermedio o avanzado
aprob = 0
d_aprob = 0
total_alumnos = 0

# porcentaje de asistencia de clase de practica hablada
p_asistencia = 0

print("Ingrese la fecha actual en formato: dia, num dia/num mes")
fecha = input("día, DD/MM: ")

# conversion del formato string al formato integer donde sea necesario
if str.isalpha(fecha[0:fecha.find(",")]) :
    if str.isdigit(fecha[fecha.find(" ")+1:fecha.find("/")]) :
        if str.isdigit(fecha[fecha.find("/")+1:]) :
            dia_sem = fecha[0:fecha.find(",")]
            dia = int(fecha[fecha.find(" ")+1:fecha.find("/")])
            mes = int(fecha[fecha.find("/")+1:])


            if dia_sem == "lunes":
                 vv = True
                 vv2 = True
            elif dia_sem == "martes":
                 vv = True
                 vv2 = True
            elif dia_sem == "miercoles":
                 vv = True
                 vv2 = True
            elif dia_sem == "jueves":
                 vv = True
                 vv4 = True
            elif dia_sem == "viernes":
                 vv = True
                 vv5 = True
            else:
                 ("error, dia de la semana mal escrito. Saliendo...")
                 
                 
            if mes%2 == 0:
                 if dia<1 or dia>31:
                     vv = False
                     print ("error. Saliendo...")
            elif mes%2 != 0:
                 if dia<1 or dia>30:
                      vv = False
                      print ("error. Saliendo...")
                    
                 if mes<1 or mes>12 :
                      vv = False
                      print ("error. Saliendo...")


            


            if vv == True:
                if vv2 == True:
                     vv3 = input("¿Se tomo examen el dia de hoy? (responder con si o no): ")
                     if vv3 == "si":
                          vv3 = True
                          aprob = int(input("aprobados: "))
                          d_aprob = int(input("desaprobados: "))
                          total_alumnos = aprob + d_aprob
                          print("El porcentaje de alumnos aprobados es el: ", aprob/total_alumnos*100, "%")


                     elif vv3 =="no":
                          vv3 = False
                          print("saliendo...")


                     elif (vv3 != "si") or (vv3 != "no"):
                               print("Error al responder si o no. Saliendo...")


                elif vv4 == True:
                     p_asistencia = int(input("ingrese el porcentaje de Asistencia sin el signo *%*: "))

                     if p_asistencia > 50:
                          print("Asistio la mayoria de alumnos")
                     else:
                          print("No asistio la mayoria")


                elif vv5 == True:
                     if dia == 1:
                          if mes==1 or mes==7:
                               print("!Inicio de nuevo ciclo¡")
                               c_alumnos = int(input("Cantidad de alumnos: "))
                               arancel = int(input("Ingrese el arancel por alumno sin el signo *$*: "))
                               ingresos_totales = c_alumnos*arancel
                               print("Se ha ingresado un total de $", ingresos_totales)


                else:
                     print("error. Se introdujo un nombre de dia, numero de dia, o numero de mes inexistente")