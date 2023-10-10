from funciones import *

#  EJERCICIO 1 **********************************************************************************************
passengers_list=[]
trips_list=[]
selection=1


while selection!=0:
    print()
    print("1. Agregar pasajero")
    print("2. Agregar destino")
    print("3. Buscar ciudad de destino por el DNI")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar pais de destino por el DNI")
    print("6. Cantidad de pasajeros que viajan a un pais pasajero")
    print("0. Salir")
    print()
    selection = int(input())

    if selection<0 and selection>6:
        print()
        print("El numero elegido no corresponde a ninguna opcion")
        continue
    if (selection==1):
        add_passenger(passengers_list)
    if (selection==2):
        add_city(trips_list)
    if (selection==3):
        lookfor_city(passengers_list, trips_list)
    if (selection==4):
        number_passengers_per_city(passengers_list)
    if (selection==5):
        lookfor_country(passengers_list, trips_list)
    if (selection==6):
        number_passengers_per_country(passengers_list, trips_list)
    if (selection==0):
        print()
        print("Saliendo...")




#  EJERCICIO 2 **********************************************************************************************
shopping = [('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),
           ('Nuria Costa', 12, 567.8, 'Calle 1 - 456'), ('Carlos Pérez', 3, 789.0, 'Calle 5 - 1223'),
           ('Teo Gonzales', 22, 1550.0, 'Calle 4 - 625') ]

addres = get_address(shopping)
print(addres)




#  EJERCICIO 3 **********************************************************************************************
partners = {
    1: {'nombre':'Amanda Núñez'    , 'fecha_ingreso':'17/03/2009' , 'cuota_al_dia':True },
    2: {'nombre':'Bárbara Molina'  , 'fecha_ingreso':'17/03/2009' , 'cuota_al_dia':True },
    3: {'nombre':'Lautaro Campos'  , 'fecha_ingreso':'17/03/2009' , 'cuota_al_dia':True },
    4: {'nombre':'Rodrigo Olguin'  , 'fecha ingreso':'26/07/2009' , 'cuota_al_dia':False},
    5: {'nombre':'Claudia Estevez' , 'fecha ingreso':'2/08/2009'  , 'cuota_al_dia':True },
    6: {'nombre':'Leonel Maratea'  , 'fecha ingreso':'5/01/2010'  , 'cuota_al_dia':False}
}


print("Sistema de gestión de socios del club.")
while True:
    print()
    print("1. Cargar datos de socios.")
    print("2. Informar cantidad de socios del club.")
    print("3. Registrar que un socio ha pagado todas las cuotas adeudadas.")
    print("4. Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018.")
    print("5. Dar de baja a un socio.")
    print("6. Imprimir el listado de socios completo.")
    print("0. Salir")
    print()
    
    selection = input("Seleccione una opción: ")
    if selection == "1":
        partenrs = cargar_socio(partners)
    elif selection == "2":
        mostrar_cantidad_socios()
    elif selection == "3":
        socio_numero = int(input("Ingrese el número del socio que ha pagado todas las cuotas: "))
        pagar_cuotas(socio_numero)
    elif selection == "4":
        partners=modificar_fecha_ingreso(partners,'13/03/2018','14/03/2018')
        print()
        print("Se actualizaron las fechas de ingreso erroneas:")
    elif selection == "5":
        name_surname = input("Ingrese el nombre y apellido del socio que desea dar de baja: ")
        partners=dar_de_baja(partners,name_surname)
        print()
        print("Se actualizo la lista de socios:")
    elif selection == "6":
        imprimir_listado(partners)
    elif selection == "0":
        break
    else:
        print("El numero ingresado no corresponde a ninguna opcion")
        continue