class Triangulo:
    def __init__ (self , side_a = 0 , side_b = 0 , side_c = 0):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c


    
    #SETTERS
    def setSideA(self , side_a):
        if isinstance(side_a , (float,int)):
            if side_a > 0:
                self.__side_a = side_a

    def setSideB(self , side_b):
        if isinstance(side_b , (float,int)):
            if side_b > 0:
                self.__side_b = side_b

    def setSideC(self , side_c):
        if isinstance(side_c , (float,int)):
            if side_c > 0:
                self.__side_c = side_c


    #GETTERS
    def getSideA (self):
        return self.__side_a
    def getSideB (self):
        return self.__side_b
    def getSideC (self):
        return self.__side_c
    

    #FUNCIONES
    # mostrar lado mayor
    def majorSide (self):
        l = self.__length
        h = self.__height
        if l > h:
            print(f"  l")
        if h > l:
            print(f"  h")
        if h==l:
            print(f"  h")
        

    # mostrar tipo de triangulo
    def type (self):
        a = self.__side_a
        b = self.__side_b
        c = self.__side_c
        if a == b and b == c:
            print("El triangulo es equilatero")
        if a == c or a == b or b == c:
            print("El triangulo es isoceles")
        if a != b and b != c:
            print("El triangulo es escaleno")