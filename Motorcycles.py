class Motorcycle:
    state = "New"
    engine = False



    def __init__ (self, color = "", regist = "", fuel_liters = 0, wheels = 0, brand = "", model = "", manufac_date = "", top_speed = 0, weight = 0):
        self.color     = color
        self.regist    = regist
        self.brand = brand
        self.model     = model
        self.weight    = weight
        self.top_speed    = top_speed
        self.manufac_date = manufac_date
        self.__private_fuel_liters  = fuel_liters
        self.__private_wheels       = wheels



    def start_up (self):
        # La funcio obtiene el estado de engine de la propia clase haciendo uso del self.engine
        if self.engine == False:
            self.engine = True
            print(" 'El motor ha arrancado'")
        else:
            print(" 'El motor ya esta en marcha'")



    
    def turn_off (self):
        if self.engine == False:
            print(" 'El motor ya esta apagado'")
        else:
            self.engine = True
            print(" 'El motor se ha apagado'")


    def getPrice (self,moto):
        return moto.price






            

firstMoto = Motorcycle("rojo" , "ade-615" , 9 , 2 , "Yamaha" , "XSR700" , "9/12/2020" , 220 , 160)
secondMoto = Motorcycle("gris platino" , "ggd-816" , 11 , 2 , "Yamaha" , "booster2023" , "16/4/2019" , 180 , 130)


print()
print("Prueba de la primer moto:")
print()
# Se inicia el encendido con el motor apagado por defeecto
firstMoto.start_up()
# Se inicia el apagado con el motor que se acaba de encender
firstMoto.turn_off()
# El motor queda apagado
print()


# Se realiza la misma prueba con la segunda moto
print("Prueba de la segunda moto:")
print()
secondMoto.start_up()
secondMoto.turn_off()
print()


print("El concesionario tiene precio para la primer motocicleta.")
# Agrego un atributo precio a la clase motocicleta.
# Este atributo solo tiene un valor asignado al objeto firstMoto
Motorcycle.price = None
firstMoto.price = 2000000
print("El precio de la primer moto",firstMoto.brand," modelo:",firstMoto.model," color:",firstMoto.color,", es de",firstMoto.price,"pesos")
print()


# Ahora, si el concesionario no hubiera anunciado el precio, se podria consultar con un metodo
# La segunda motocicleta no podra hacer uso del atributo, porque este fue asignado a la primera. Se debe asignar uno a la segunda}

# Le pasamos el objeto a la funcion y la funcion nos devuelve el valor del atributo del objeto
print("La consulta del precio de la primer moto nos dice que la moto cuesta:")
print("",firstMoto.getPrice(firstMoto))
print()
# Al no tener valor, el atributo precio en el objeto secondMoto, esta nos devuelve "none"
print("La consulta del precio de la primer moto nos dice que la moto cuesta:")
print("",secondMoto.getPrice(secondMoto))
print()
