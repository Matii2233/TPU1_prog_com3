# Funcion ingresar numeros en una lista
def input_nums(nums):
    while True:
        num = int(input("> "))
        
        if num == 0:
            break  
        else:
            nums.append(num)

    print()
    return nums


#Funcino borrar un numero, ingresado por el usuario, de la lista
def erase_num(nums,num):
    for i in range(len(nums)):
        if num == nums[i]:
            del nums[i]
            return nums
        
    print("El numero no se pudo borrar, porque no esta en la lista")
    return nums



# Funcion sumar el total de los numeros de la lista
def total(nums):
    acumulator = 0
    for num in nums:
        acumulator += num

    return acumulator


# Funicion crear lista con los numeros de la lista original menores que un numero que ingrese el usuario
def lowers_nums(nums,num,new_list):
    for i in nums:
        if i<num:
            new_list.append(i)
        
    return new_list


def show_newlist(new_numslist):
    print("[",end="")
    for num in new_numslist:
        print("",num,end=" ")
    print("]",end="")


def get_pairs_nums_and_currencys(nums,pairslist):
    currency = 0
    pair = 0

    for i in nums:
        for j in nums:
            if i==j:
                currency +=1
        
        pair = (i,currency)
        pairslist.append(pair)

    return pairslist