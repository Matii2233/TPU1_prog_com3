def merge (arr) :
    if len(arr) == 1 :
        return arr
    
    midValue = len(arr)//2
    left = arr[:midValue]
    rigth = arr[midValue:]

    left = merge(left)
    rigth = merge(rigth)

    return mergeSort(left,rigth)

def mergeSort (left,rigth):
    ordList = []
    while len(left)>0 and len(rigth)>0 :
        if left[0] < rigth[0]:
            ordList.append(left[0])
            left=left[1:]
        else:
            ordList.append(rigth[0])
            rigth=rigth[1:]

    if len(left)>0:
        ordList = ordList + left
    if len(rigth)>0:
        ordList = ordList + rigth

    return ordList


arr=[3,14,66,2,7,53,23,39,53,26,99,37,12,21,77]
print()
print("la lista original es:")
print("", arr)

print()
print("La lista ordenada es")
print("", merge(arr))