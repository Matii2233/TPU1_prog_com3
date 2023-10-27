def input_nums(nums):
    while True:
        num = int(input("Ingrese un número: "))
        if num == 0:
            break
        nums.append(num)

    return nums


def get_minors_list(nums, num):
    minors = []
    for n in range(len(nums)):
        if nums[n] < num:
            minors.append(nums[n])

    return minors





# PUNTO 1 **********************************************************************************************************************************
# Ingresar numeros enteros a una lista vacia y mostrar la lista. Se acabar el proceso al ingresar "0"
nums = []

print("Ingresa numeros a la lista (0 para salir)")
nums = input_nums(nums)

print("Números ingresados:",nums)
print()


# PUNTO 2 **********************************************************************************************************************************
# Eliminar un numero de la lista que sea ingresado por el usuario y mostrar la lista actual. 
# Validar que el numero ingresado este en la lista
if nums:
    num = int(input("Numero a eliminar: "))
    if num in nums:
        nums.remove(num)
        print("Se ha eliminado el numero",num,"De la lista")
        print()
        print("Lista actual:")
        print(nums)
    else:
        print("el numero ingresado no existe en a lista")
print()


# PUNTO 3 **********************************************************************************************************************************
# Sumar todos los numeros de la lista en una variable y mostrar el resultado
if nums:
    sum = sum(nums)
    print("La suam de los valores de la lista es:",sum)
print()


# PUNTO 4 **********************************************************************************************************************************
# Crear una lista de numeros, procedentes de la lista original, menores que un numero ingresado por el usuario y mostrarla.
if nums:
    newNum  = int(input("Ingrese un nuevo numero: "))
    newList = get_minors_list(nums, newNum)
    print()
    print("La nueva lista de numeros menores es:")
    print(newList)


# PUNTO 5 **********************************************************************************************************************************
# Crear una lista compuesta de tuplas de numeros parejas, las cules seran los numeros de la lista original y su ocurrencia en la misma.
if nums:
    numsOcurrences = {}
    for num in nums:
        if num in numsOcurrences:
            numsOcurrences[num] += 1
        else:
            numsOcurrences[num] = 1

couples = []
for number, frequency in numsOcurrences.items():
    couples.append((number, frequency))

print("La nueva lista es:")
print(couples)
print()


# PUNTO 6 **********************************************************************************************************************************
students = []
repeateds = []

print("Ingrese los alumnos  de Nivel Primario")
while True:
    name = input("Nombre del alumno: ")
    if name == "x" or name == "X":
        break
    students.append(name)

print("Ingrese los alumnos de Nivel Secundario")
while True:
    name = input("Nombre del alumno: ")
    if name == "x" or name == "X":
        break
    if name in students:
        repeateds.append(name)
    else:
        students.append(name)

primary = students[:]

print("Los alumnos de nivel primario y secundario son:")
print(students)
print()
print("Los nombres de los alumnos que se repiten son:")
print(repeateds)

primaryNotRepeateds = []
for name in primary:
    if name not in students:
        primaryNotRepeateds.append(name)

print("Los nombres de nivel Primario que no se repiten en el nivel Secundario son:")
print(primaryNotRepeateds)
print()


# PUNTO 7 **********************************************************************************************************************************
# Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings.
# Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados."""

times = {}

for i in range(5):
    string = input("Ingrese una palabra: ")
    
    for char in string:
        if char in times:
            times[char] += 1
        else:
            times[char] = 1

print("Cantidad total de ocurrencias de cada carácter:")
for char, count in sorted(times.items()):
    print(char,":",count)
print()




# PUNTO 8 **********************************************************************************************************************************
# En una liga inter barrial hay equipos enumerados del 1 al 10 que compiten todos contra todos. 
#  - lea el cuadro de goles en un arreglo de 2 dimensiones
#  - muestra victorias derrotas y empates para cada equipo
#  - muestra la diferencia de goles anotados y recibidos
#  - determine los puntos obtenidos de cada equipo

goals = [
    [0, 4, 2, 1],
    [5, 0, 3, 2],
    [0, 2, 0, 1],
    [1, 0, 2, 0]
]

numTeams = len(goals)

points = {team: 0 for team in range(1, numTeams + 1)}

for homeTeams in range(1, numTeams + 1):
    for awayTeams in range(1, numTeams + 1):
        if homeTeams != awayTeams:
            homeGoals = goals[homeTeams - 1][awayTeams - 1]
            awayGoals = goals[awayTeams - 1][homeTeams - 1]

            if homeGoals > awayGoals:
                points[homeTeams] += 3
            elif homeGoals == awayGoals:
                points[homeTeams] += 1
                points[awayTeams] += 1
            else:
                points[awayTeams] += 3

for team, totalPoints in points.items():
    print("Equipo",team,":Puntos =",totalPoints)

for homeTeams in range(1, numTeams + 1):
    goalsScored = sum(goals[homeTeams - 1])
    goalsRecived = sum(goals[homeTeams - 1][i] for i in range(numTeams))
    goalDiff = goalsScored - goalsRecived
    print("Equipo",homeTeams,": Diferencia de goles =",goalDiff)
print(" ")


# PUNTO 9 **********************************************************************************************************************************
# Simula el juego memotest, que consiste en una baraja de cartas dadas vueltas y se deben encontrar todas las parejas
import copy
def showBoard(board):
    pos = 1
    coords2 = {1:'a', 2:'b', 3:'c', 4:'d'}
    print(end='    ')

    for i in range(1,5):
        print(coords2[pos], end = '   ')
        pos += 1
    print("")
    pos = 1
    for i in board:
        print(pos, end='   ')
        for j in i:
            print(j, end = '   ')
        pos +=1
        print("")


def boardState(board):
    stateBoolean = True
    for i in board:
        for j in i:
            if j == 'X':
                return False
    return stateBoolean


def card_input():
    userCoord = input("Ingrese una posición (EJ: b3): ").lower()

    while userCoord[0] not in coords.keys() or int(userCoord[1]) not in coords.values():
        userCoord = input("Ingrese una posición valida: ").lower()

    while currentBoard[int(userCoord[1])-1][coords[userCoord[0]]] != 'X':
        userCoord = input(f"La carta en las coordenadas {userCoord} ya ha sido revelada: ").lower()

        while userCoord[0] not in coords.keys() or int(userCoord[1]) not in coords.values():
            userCoord = input("Ingrese una posición valida: ").lower()

    while currentBoardAux[int(userCoord[1])-1][coords[userCoord[0]]] != 'X':
        userCoord = input(f"Ya has seleccionado esa carta: ").lower()

        while userCoord[0] not in coords.keys() or int(userCoord[1]) not in coords.values():
            userCoord = input("Ingrese una posición valida: ").lower()
    return userCoord

coords = {'a':0, 'b':1, 'c':2, 'd':3}
currentBoard = [
    ['X','X','X','X'],
    ['X','X','X','X'],
    ['X','X','X','X']]
currentBoardAux = copy.deepcopy(currentBoard)
cards = [
    [1,4,3,2],
    [6,6,5,1],
    [2,5,4,3]]
completeBoard = boardState(currentBoard)

print("Bienvenido a Memotest!")
print("Encuentra todos los pares del tablero para ganar el juego!")
print("El tablero a resolver es el siguiente: ")
print("")
while completeBoard == False:
    already_selected = False
    showBoard(currentBoard)
    print("")
    input_coord = card_input()
    column = input_coord[0]
    column = coords[column]
    row = int(input_coord[1])-1
    currentBoardAux[row][column] = cards[row][column]
    first_selected = currentBoardAux[row][column]
    showBoard(currentBoardAux)
    print("")
    input_coord = card_input()
    column = input_coord[0]
    column = coords[column]
    row = int(input_coord[1])-1
    currentBoardAux[row][column] = cards[row][column]
    last_selected = currentBoardAux[row][column]
    showBoard(currentBoardAux)
    if last_selected == first_selected:
        print("Has encontrado un par!")
        print("")
        currentBoard = copy.deepcopy(currentBoardAux)
    else:
        print("No se ha encontrado un par")
        print("")
        currentBoardAux = copy.deepcopy(currentBoard)
    completeBoard = boardState(currentBoard)

print("Has ganado! Felicidades!")
print(" ")


# PUNTO 10 
# Teniendo una matriz cuadrada de cualquier dimensión, obtener la diagonal principal y la diagonal inversa
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

princ = []
for i in range(len(matriz)):
    princ.append(matriz[i][i])

inv = []
for i in range(len(matriz)):
    inv.append(matriz[i][len(matriz) - 1 - i])


print("La diagonal principal tiene los valors:")
print(princ)
print()
print("La diagonal inversa tiene los valores:")
print(inv)

# PUNTO 11 *********************************************************************************************************************************
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
divisas = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
divisaData = input("Ingrese una divisa ('Euro', 'Dolar' o 'Yen'): ")

for divisa, symbol in divisas.items():
    if divisa in divisas:
        symbol = divisas[symbol]
        print("El símbolo del ",divisaData,"es",symbol)
    else:
        print("La divisa ingresada no se encuentra en la lista")
    print()


# ingresar nombre, edad, direccion y telefono del usuario en un diccionario y luego mostrar los datos
name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
adress = input("Ingrese su dirección: ")
phone = input("Ingrese su número de teléfono: ")

userData = {
    "Nombre" : name,
    "Edad" : age,
    "Dirección" : adress,
    "Telefono" : phone
}

print("El nombre es:",userData["Nombre"])
print("La edad es:",userData["Edad"])
print("La direccion es:",userData["Dirección"])
print("El telefono es:",userData["Telefono"])


# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
print("----------13----------")
fruits = {"Manzana": 80, "Naranja": 100, "Banana": 120, "Durazno": 120}

userFruit = input("¿Qué fruta le gustaría comprar?: ").title()
if userFruit in fruits:
    fruitKg = float(input("¿Cúantos Kilos desea?: "))
    total = fruits[userFruit] * fruitKg
    print("Usted desea comprar",fruitKg,"Kilos de",userFruit)
    print("El total es de: $",total)
else:
    print("La fruta seleccionada no se encuentra en la lista")