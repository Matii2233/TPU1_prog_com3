#FUNCION PUNTO 1
def validation (id):
    #primero se comprueba que el dni se componga solo de numeros
    if isinstance(id, int):
        if len(str(id))>=7 and len(str(id))<=8:
            return True
        else:
            return False
    else:
        print("El DNI debe componerse unicamente de numeros")





#FUNCION PUNTO 2
def last_word_lenght(text):
    splittext=text.split()

    return len(splittext[-1])





#FUNCION PUNTO 3
def id_obtaining(fullname,dni):
    fullname_to_list=fullname.split()
    print(fullname_to_list)
    id=fullname_to_list[0]
    surname_lenght=len(fullname_to_list[-1])
    if len(dni)==7:
        dni_digits=int(dni)//10000
    if len(dni)==8:
        dni_digits=int(dni)//100000
    id+=str(surname_lenght)
    id+=str(dni_digits)

    return id





# FUNCIONES PUNTO 4
def is_mult(number1,number2):
    if number1%number2==0:
        return True
    elif number2%number1==0:
        return True
    else:
        return False


def the_first_is_mult(numbera,numberb):
    if numbera==numberb:
        return False
    if numbera%numberb==0:
        return True
    else:
        return False





# FUNCION PUNTO 5
def temp_average(temp1,temp2):
    return (temp1+temp2)/2





# FUNCION PUNTO 6
def text_modifier(text,obtainedtext):
    # en el ciclo for, se recorre cada caracter de la cadena
    for letter in text:
        # al mismo tiempo cada caracter se guarda en una nueva variable seguido de un espacio
        obtainedtext+=letter+" "
    
    return obtainedtext





#FUNCION PUNTO 7
def obtain_max_and_min(nums_list):
    max=0
    min=nums_list[0]
    for num in nums_list:
        if num>max :
            max=num
        if num<min :
            min=num

    return min, max





#FUNCION PUNTO 8
def obt_area_perimeter(r):
    pi=3.14

    area      = pi*(r**2)
    perimeter = 2*pi*r

    return area,perimeter





#FUNCION PUNTO 9
def login(username,password,tries):
    access = False
    if username == "usuario1":
        if password == "asdasd":
            access=True

    if access == False:
        tries+=1

    return access,tries





#FUNCION PUNTO 10
def apply_discount(costs):
    total_cost =   costs["cost1"]*(1-costs["discount1"])   +   costs["cost2"]*(1-costs["discount2"])   +   costs["cost3"]*(1-costs["discount3"])
    return total_cost





#FUNCIONES PUNTO11
def get_absolute_value(num):
    if num>=0:
        return num
    if num<0:
        return num*(-1)
    

def apply_absolute_value(nums):
    absolute_values=[]
    for num in nums:
        absolute_values.append(get_absolute_value(num))

    return absolute_values





#FUNCION PUNTO 12
def text_to_dictionary(text):
    words_dictionary={}
    text = text.split()
    i=0
    for word in text:
        i+=1
        words_dictionary["palabra "+str(i)] = word

    return words_dictionary,len(words_dictionary)





#FUNCION PUNTO 13
def get_module(nums):
    modules=[]

    for num in nums:
        modules.append(num%2)

    return modules





# funcion punto 14
def prime_nums(num):
    if num<=1:
        return False  
    if num==2 or num==3:
        return True
    if num>3:
        for i in range(2 , int(num**0.5) + 1):
            if num % i == 0:
                return False
            else:
                return True





#FUNCIONES PUNTO 15
def input_nums(acumulator):
    num = int(input("numero: "))
    acumulator += 1

    return num, acumulator


def get_factorial(num):
    if num < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif num == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        return resultado
    




#FUNCION PUTNTO 16
def get_currencys(num, digit):
    currencys = 0
    
    # utilizo variables para guardar los numeros como string
    num_str = str(num)
    digit_str = str(digit)
    
    # se utilizan las variables string para poder usar un ciclo for
    for d in num_str:
        if d == digit_str:
            currencys += 1
    
    return currencys





# FUNCIONES PUNTO 17 
#   primo o no
def prime_nums(num):
    if num<=1:
        return False  
    if num==2 or num==3:
        return True
    if num>3:
        # el rango que se recorrera es (desde: 2 ,  hasta: raizCuadrada de 'num' + 1)
        # si desde 2 hasta la raiz cuadrada del numero + 1 no hay divisores, entonces el numero es primo (funcion=True)
        for i in range(2 , int(num**0.5) + 1):
            if num % i == 0:
                return False
            else:
                return True
    


#   validacion de digito
def digit_validation(digit, digit_lenght):
    # variable 'digit_lenght' para comrpobar que se ingrea solo un digito
    if digit_lenght>1:
        print("Se debe ungresar UN SOLO digito")
        print()
        
        # ciclo while que no acaba hasta que se ingresa un solo digito en 'digit'
        while digit_lenght>1:
            print("Ingresa otro digito:")
            digit=int(input())
            digit_lenght = len(str(digit))
            print()
    
    return digit,digit_lenght



#   mostrar suma de los digitos 
def show_digits_sum(num):
    digits_sum=0
    str_num = str(num)
    for d in str_num:
        digits_sum+=int(d)

    return digits_sum



#   funcion obtener ocurrencia 
def get_currencys(num, digit):
    currencys = 0
    num_str = str(num)
    digit_str = str(digit)
    
    for d in num_str:
        if d == digit_str:
            currencys += 1
    
    return currencys



#   obtener factorial 
def get_factorial(largestnum):
    if largestnum < 0:
        return "No se puede calcular el factorial de un número negativo"
    elif largestnum == 0:
        return 1
    else:
        #se supone que el resultado sera al menos  '1'  y se guarda en  'resultado'
        resultado = 1

        for i in range(1, largestnum+1):
            resultado *= i
        return resultado