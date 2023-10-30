from funciones import is_power_bool

print()
expo = 100
base = 10

# Para comprobar, de forma aritmetica, que los numeros sean enteros use esta condicion
if expo % 1 == 0 and base % 1 == 0:
    isPower = is_power_bool(expo, base)

    if isPower:
        print(f"El numero {expo} es potencia de {base}")
    else:
        print(f"El numero {expo} no es potencia de {base}")
else:
    print("Los numeros deben ser enteros")
print()