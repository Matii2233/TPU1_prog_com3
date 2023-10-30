from funciones import get_max_num

# Escribir una función recursiva que encuentre el mayor elemento de una lista.

print()
nums = [2,6,12,3,22,23,12,1,32,77,16]
maxNum = nums[0]
print(f"La lista es")
print(nums)
print(f"El elemento mayor de la lista es:")
print(get_max_num(nums, maxNum))
print()