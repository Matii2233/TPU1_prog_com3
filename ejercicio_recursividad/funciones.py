import random

# FUNCION ejercicio 1
def get_departure_time():
    path_choosed = random.randint(1, 3)
    
    if path_choosed == 3:
        return 7
    
    turn_time = 0
    
    if path_choosed == 1:
        turn_time = 3
    elif path_choosed == 2:
        turn_time = 5
    
    remaining_time = turn_time + get_departure_time()
    return remaining_time


# FUNCION ejercicio 2
def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))