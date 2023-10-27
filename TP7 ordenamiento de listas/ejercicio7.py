def separate_list (dataList) :
    numsList=[]
    letterslist=[]

    for i in dataList:
        if isinstance(i,(int,float)):
            numsList.append(i)
        if isinstance(i,str):
            letterslist.append(i)
        if isinstance(i,bool):
            print("El valor",i,"no seguardo en la nueva lista porque no es numero ni texto")
        
    dataList = numsList
    dataList = dataList + letterslist
    
    return dataList


dataList = ["a" , "alberto" , 2 , 8.9 , "folers en el parque" , 77 , 3.1416 , "b" , 1234 , "c" , "casa" , 1.5]
print()
print("Los contenidos de la lista original son:")
print(" ",dataList)
print()

print("La lista ordenada con numeros y luego strings es:")
orderedList = []
orderedList = separate_list(dataList)
print(" ",orderedList)
print()