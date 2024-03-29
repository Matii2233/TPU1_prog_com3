from funciones import get_departure_time

# Escribir una función que simule el siguiente experimento: Se tiene una rata en una jaula con 3 caminos,
# entre los cuales elige al azar (cada uno tiene la misma probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, 
# si elige el 2 luego de 5 minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
# La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero quiere su libertad, 
# por lo que recorrerá los caminos hasta salir de la jaula. La función debe devolver el tiempo que tarda la rata en salir de la jaula.

print(f"El raton tardo {get_departure_time()} minutos en salir de la jaula.")