from funciones import find_positions

# Escribir una funcion recursiva que reciba como parámetros dos strings a y b, 
# y devuelva una lista con las posiciones en donde se encuentra b dentro de a

print()
string_a = "abracadabra pata de cabra" # Cadena de palabras
string_b = "abra"                      # Palabra a buscar
positions = find_positions(string_a, string_b)
print(f"Desde:   0")
print(f"Hasta:   {len(string_a)}")
print(f"palabra: {string_b}")
print()
print("Las posiciones donde se encuentra la palabra buscada son:")
print(f"  {positions}")
print()