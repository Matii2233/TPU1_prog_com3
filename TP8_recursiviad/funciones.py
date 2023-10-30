# FUNCION ejercicio 1
def countDigits(num, digitCounter):
    if len(num) == 1:
        # Cuando el numero solo tiene un digito, se devuelve el valor obtenido por el contador de digitos
        return digitCounter
    # Cada digito contado (digitCounter+1) se elimina del numero original (num[1:]) para que no se vuelva a contar
    digitCounter = countDigits(num[1:],digitCounter+1)
    return digitCounter


# FUNCION ejercicio 2
def is_power_bool(expo,base):

    # Condicion de salida, cuando se halla dividido el numero mayor hasta ser igual a 1, se devuelve TRUE
    if expo == 1:
        return True
    
    expo = expo/base
    
    # Si "expo/base" dio un numero divisible por "base" se vuelve a entrar en la funcion
    if expo%1==0:
        is_power_bool(expo,base)
        return True
    # Si una division, dio un numero 'expo' no multiplo de 'base', entonces expo no es potencia de base, y la funcion devuelve "false"
    else:
        return False
    

# FUNCION ejercicio 3
def find_positions(a, b, start=0, positions=None):
    if positions is None:
        positions = []
    
    # Encuentra la primera ocurrencia de b en a a partir de la posición "start"
    index = a.find(b, start)
    
    # Cuando se encuentra la palabra buscada se agrega a la lista correspondiente
    # Tambien se actualiza la posicion de inicio (Start) para la proxima llamada recursiva
    if index == -1:
        return positions
    else:
        positions.append(index)
        start = index + 1
        return find_positions(a, b, start, positions)


# FUNCION ejercicio 4 
def par(n):
    if n == 0:
        print(f"El numero {n} es par.")
    elif n%2 == 0:
        print(f"El numero {n} es par.")
    else:
        return impar(n)
def impar(n): 
    if n == 1:
        print(f"El numero {n} es impar.")
    elif n%2 != 0:
        print(f"El numero {n} es impar.")
    else:
        return par(n)
    

# FUNCION Ejercicio 5
def get_max_num(nums, maxNum):
    if len(nums) == 1:
        return maxNum
    nums = nums[1:]
    if maxNum < nums[0]:
        maxNum = nums[0]
    maxNum = get_max_num(nums, maxNum)
    return maxNum


# FUNCION ejercicio 6
def get_ocurrences_list(values, ocurrences, replics_list):
    if len(values) == 1:
        for i in range(ocurrences):
            replics_list.append(values[0])
        return replics_list
    for i in range(ocurrences):
        replics_list.append(values[0])
    return get_ocurrences_list(values[1:], ocurrences, replics_list)


# FUNCION ejercicio 7
def get_K(n, p):
    if n == 1:
        return p
    else:
        return n * p + get_K(n - 1, p)
    

# FUNCION ejercicio 8
def get_pascals_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(get_coeficient(i, j), end=" ")
        print()
def get_coeficient(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return get_coeficient(n - 1, k - 1) + get_coeficient(n - 1, k)
    

# Funcion punto 9
def couples(chars, k, this_chain="", result=[]):
    if k == 0:
        result.append(this_chain)
    else:
        for c in chars:
            couples(chars, k - 1, this_chain + c, result)

def get_couples(chars, k):
    result = []
    couples(chars, k, "", result)
    for chain in result:
        print(chain)


# FUNCION punto 10
def get_sheet_dimensions(n):
    # Caso base
    if n == 0:
        return (841, 1189)  # Medidas de la hoja A0 en milímetros (ancho, largo)
    else:
        # Llama a la función de manera recursiva con N-1
        previous_width, previous_length = get_sheet_dimensions(n - 1)
        
        # Calcula las medidas de la hoja A(N) a partir de A(N-1)
        new_width = previous_length / 2
        new_length = previous_width
        
        return (new_width, new_length)