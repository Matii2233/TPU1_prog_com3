def byCount(arr):
    maxim = max(arr)
    minim = min(arr)
    valuesRange = maxim - minim + 1
    count =  [0] * valuesRange

    for n in arr:
        count[n - minim] += 1

    ordererList = []
    for i in range(valuesRange):
        for j in range(count[i]):
            ordererList.append(i + minim)

    return ordererList



myList = [23,55,2,15,67,4,8,12,55]
ordererList = byCount(myList)
print(ordererList)