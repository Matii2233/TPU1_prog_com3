class Cuenta:
    def __init__ (self , owner = "'Nadie'" , money = 0):
        self.__owner = owner
        self.__money = money

    
    #SETTERS
    def set_owner(self , owner):
        if isinstance(owner , str):
            self.__owner = owner
    def deposit_money(self , quantity):
        if isinstance(quantity , (int , float)):
            if quantity >= 0:
                self.__money += quantity
    def withdraw_money (self, quantity):
        if isinstance(quantity , (int , float)):
            self.__money -= quantity
    

            

    #GETTERS
    def get_owner(self):
        return self.__owner
    def get_money(self):
        return self.__money
    

    #FUNCIONES
    def show_info (self):
        print(f"  Titular: {self.get_owner()}")
        print(f"  Monto: {self.get_money()}")
