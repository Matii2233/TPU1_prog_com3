from funciones import get_ocurrences_list

# Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. 
# Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])

print()
# Tupla con la lista y la cantidad de repeticiones para cada valor
nums_ocurrence = ([1,5,5,12,8,8,8] , 2)
print(f"En la lista: ")
print("", nums_ocurrence)
print(f"Debera repetirse {nums_ocurrence[1]} veces cada valor")

values       = nums_ocurrence[0]
ocurrences   = nums_ocurrence[1]
replics_list = []
print("La lista resultante es:")
print(get_ocurrences_list(values, ocurrences, replics_list))
print()