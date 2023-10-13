from dimensionadas_funciones import *

# PUNTO 1 ****************************************************************************************************
# Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar 
# el usuario debe ingresar 0, el cual no debe guardarse.

nums = []

print("Ingresa números para llenar una lista (0 para finalizar): ")
print(input_nums(nums))
print()

print("Ingresa un numero que quieras borrar de la lista")
num  = int(input("> "))
print()

nums = erase_num(nums,num)
print(nums)
print()

print("La suma total de los numeros de la lista es:",total(nums))
print()
print("Ingrese un numero nuevamente")
num = int(input("> "))
print()

new_numslist = []
new_numslist = lowers_nums(nums,num, new_numslist)

print("La lista de numeros menores que el numero ingreasdo es:")
show_newlist(new_numslist)

