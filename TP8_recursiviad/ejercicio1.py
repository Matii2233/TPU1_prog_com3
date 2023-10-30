from funciones import countDigits

# escribe una funcion que reciba un numero positivo "n" y devuelva la cantidad de digitos de "n"
print()
positiveNum = 43521
digitCounter = 1
num = []
for n in str(positiveNum):
    num += n
digits = countDigits(num, digitCounter)
print(f"El numero {positiveNum} tiene {digits} digitos")
print()