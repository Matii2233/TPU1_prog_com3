from funciones import get_K

# Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p

n = int(input("Ingrese un numero entero: "))
p = int(input("Ingrese un numero entero: "))

result = get_K(n, p)
print(f"El resultado de  'K(n,p) = p + 2p + 3p ... + np'  es:")
print("", result)