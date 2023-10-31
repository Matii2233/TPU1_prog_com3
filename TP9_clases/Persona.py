#Clase persona ejercicio 1
class Persona:
    def __init__ (self, name="'Vacio'", age=0, dni=0):
        self.__name = name
        self.__age = age
        self.__dni = dni


    #GETTERS
    def get_name (self):
        return self.__name
    def get_age (self):
        return self.__age
    def get_dni (self):
        return self.__dni


    #SETTERS
    def set_name(self, name):
        if isinstance(name , str):
            self.__name = name
        else:
            self.__name = "ERROR 'el nomrbe debe ser tipo texto'"
    def set_age(self, age):
        if isinstance(age , int):
            if age>0:
                self.__age = age
    def set_dni(self, dni):
        if isinstance(dni , int):
            self.__dni = dni

    
    #FUNCIONES DE 'PERSONA'
    def show_persona (self):
        print(f"  Nombre: {self.get_name()}")
        print(f"  Edad: {self.get_age()}")
        print(f"  DNI: {self.get_dni()}")
    def is_legal_age (self):
        if self.__age == 0:
            print("La edad es nula")
        else:
            if self.__age > 17:
                return True
            else:
                return False