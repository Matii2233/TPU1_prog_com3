class Agenda:
    def __init__ ( self , contacts=[] , contact=[] , name="'VACIO'" , mail="'VACIO'" , number=0 ):
        self.__contacts = contacts
        self.__contact = contact
        self.__name = name
        self.__mail = mail
        self.__number = number


    #AÑADIR CONTACTO
    def add_contact (self):
        self.__contact = {"nombre" : self.add_name(),
                          "numero" : self.add_number(),
                          "mail"   : self.add_mail()}
        self.__contacts.append(self.__contact)

    def add_name (self):
        self.__name = input("  nombre: ")
        return self.__name
    
    def add_number(self):
        self.__number = input("  numero: ")
        return self.__number
    
    def add_mail (self):
        self.__mail = input("  correo: ")
        return self.__mail


    #LISTA DE CONTACTOS
    def get_contact (self , n):
        return self.__contacts[n]
    
    def get_contacts (self):
        for i in self.__contacts:
            print(f"  {i}")


    #BUSCAR CONTACTO
    def search(self, name):
        if isinstance(name , str):
            for contact in self.__contacts:
                for c in contact:  
                    value = contact[c]
                    if value == name:
                        print("Contacto buscado:")
                        print(f"  {contact}")


    #EDITAR CONTACTO
    def edit(self, name):
        if isinstance(name, str):
            for contact in self.__contacts:
                if "nombre" in contact and contact["nombre"] == name:
                    contact["nombre"] = self.add_name()
                    contact["numero"] = self.add_number()
                    contact["mail"] = self.add_mail()
                    print(f"Contacto '{name}' editado.")
                    return
            print(f"Contacto '{name}' no encontrado.")
        else:
            print("Nombre incorrectamente ingresado")
