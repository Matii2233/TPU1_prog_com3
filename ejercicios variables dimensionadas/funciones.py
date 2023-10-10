#  FUNCIONES EJERCICIO 1 *************************************************************************************
# funcion 1 agregar pasajeros a la lista de pasajeros
def add_passenger(passengers_list):
    name = input("Nombre del pasajero: ")
    dni = int(input("DNI del pasajero: "))
    destination = input("Destino del pasajero: ")
    passengers_list.append((name, dni, destination))
    print("Pasajero agregado correctamente.")


# Función 2 agregar ciudades a la lista de destinos
def add_city(trips_list):
    city = input("Nombre de la ciudad: ")
    country = input("Nombre del país al que pertenece: ")
    trips_list.append((city, country))
    print("Ciudad agregada correctamente.")


# funcion 3 buscar ciudad por el dni del pasajero
def lookfor_city(passengers_list,trips_list):
    dni = int(input("Ingrese el DNI del pasajero: "))
    for passenger in passengers_list:
        if passenger[1] == dni:
            for city in trips_list:
                if passenger[2] == city[0]:
                    print("El pasajero viaja a la ciudad de", {city[0]}, {city[1]})
                    return
    print("Pasajero no encontrado.")


# funcion 4 cantidad de pasajeros que viajan a una ciudad
def number_passengers_per_city(passengers_list):
    city = input("Ingrese el nombre de la ciudad: ")
    count = 0
    for passenger in passengers_list:
        if passenger[2] == city:
            count += 1
    print("La cantidad de pasajeros que viajan a",{city},"es:",{count})


# funcion 5 buscar pais por dni
def lookfor_country(passengers_list,trips_list):
    dni = int(input("Ingrese el DNI del pasajero: "))

    for passenger in passengers_list:
        if passenger[1] == dni:
            for city in trips_list:
                if passenger[2] == city[0]:
                    print(f"El pasajero viaja a {city[1]}.")
                    return
    print("Pasajero no encontrado.")


# funcion 6 cantidad de personas que viajan a un pais
def number_passengers_per_country(passengers_list, trips_list):
    country = input("Ingrese el nombre del país: ")
    count = 0
    for passneger in passengers_list:
        for city in trips_list:
            if passneger[2]==city[0] and city[1]==country:
                count += 1
    print("La cantidad de pasajeros que viajan a",{country},"es:",{count})






#  FUNCIONES EJERCICIO 2 *************************************************************************************
def get_address(shopping):
    # Crear un conjunto para almacenar domicilios únicos
    only_address = set()

    # Iterar sobre la lista de compras
    for buys in shopping:
        # compra devuelve 4 valores, por lo que se debe guardar solo el de la cuarta posicion con nombre "address"
        _, _, _, address = buys
        only_address.add(address)

    # se convierten los domicilios a una lista de domicilios
    address_list = list(only_address)

    return address_list






#  FUNCIONES EJERCICIO 3 *************************************************************************************
# funcion 1 CARGAR nuevos datos de los socios
def cargar_socio(partners):
    num = int(input("Numero de socio:"))
    if num in partners:
        return "El numero de socio ya extiste. ingrese un num que no coincida con uno ya existente"
    
    name       = input("Nombre de socio: ")
    entry_date = input("Fecha de ingreso")
    fee_paid   = bool(input("Cuota al dia. Si o no: "))
        
    partners[num].append({'nombre': name, 'fecha_ingreso': entry_date, 'cuota_al_dia': fee_paid})
    return partners


# Función 2 para MOSTRAR la cantidad de socios
def mostrar_cantidad_socios(partners):
    print("La cantidad de socios es:",{len(partners)})


# Función 3 para marcar que un socio ha PAGADO todas las CUOTAS adeudadas
def pagar_cuotas(partners):
    partner_num=int(input("Numero de socio: "))

    if partner_num in partners:
        partners[partner_num]["cuota_al_dia"] = True
        print("El socio n°",{partner_num},"ha pagado todas las cuotas adeudadas.")
    else:
        print("No se encontró al socio n°",{partner_num})


# Función 4 para MODIFICAR la fecha de ingreso de los socios
def modificar_fecha_ingreso(partners,date, new_date):
    for partner_id, partner_data in partners.items():
        if partner_data.get('fecha_ingreso') == date:
            partner_data['fecha_ingreso'] = new_date
    
    return partners


# Función 5 para DAR DE BAJA a un socio
def dar_de_baja(partners,name_surname):
    for key, data in partners.items():
        if data.get("nombre") == name_surname:
            del partners[key]
            return partners
    else:
        print("No se encontró al socio",name_surname)


# Función 6 para MOSTRAR el listado de socios completo
def imprimir_listado(partners):
    print("Listado de socios:")
    for key,data in partners.items():
            print(key,":",data)