# Funcion ordenamiento burbuja ascendente
def bubble_sort (arr):
    # Se usan dos indices para comparar un numero con todos los demas de la lista y poner al menor en el lugar del primer indice
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]<arr[j]:
                aux = arr[i]
                arr[i] = arr[j]
                arr[j] = aux
    
    return arr




# main
nums = [34,12,3,45,23,11,40,27,39,20,5,9]
print("Lista original:")
print(nums)
print()
print("Lista ordenada por metodo BURBUJA:")
print(bubble_sort(nums))
