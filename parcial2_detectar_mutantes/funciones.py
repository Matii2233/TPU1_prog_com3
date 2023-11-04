import random

# FUNCION DETECTAR MUTANTE
def is_mutant (dna):
    coincidences = 0
    coincidences = detect_horizontal_patterns(dna, coincidences)
    coincidences = detect_vertical_petterns(dna, coincidences)
    coincidences = detect_diagonal_petterns(dna, coincidences)
    if coincidences > 1:
        return True
    else:
        return False
    

    



# FUNCION DETECTAR PATRONES HORIZONTALES
def detect_horizontal_patterns(dna, coincidences):
    for i in range(6):
        for j in range(3):
            letter = dna[i][j]
            if letter == dna[i][j+1]:
                if letter == dna[i][j+2]:
                    if letter == dna[i][j+3]:
                        coincidences += 1
                        break
    return coincidences

    




# FUNCION DETECTAR PATRONES VERTICALES
def detect_vertical_petterns(dna, coincidences):
    for j in range(6):
        for i in range(3):
            letter=dna[i][j]
            if letter == dna[i+1][j]:
                if letter == dna[i+2][j]:
                    if letter == dna[i+3][j]:
                        coincidences += 1   
                        break
    return coincidences






# FUNCION DETECTAR PATRONES DIAGONALES
def detect_diagonal_petterns(dna, coincidences):
    # de arriba a abajo e izquierda a derecha
    pos=[]
    for i in range(3):
        for j in range(3):
            if [i,j] not in pos: # si la posicion actual esta en una posicion ya encontrada, se pasa a la siguiente posicion #
                letter = dna[i][j]
                if letter == dna[i+1][j+1]: # una cadena de ifs que buscan que el patron de coincidencias sea diagonal #
                    if letter == dna[i+2][j+2]:
                        if letter == dna[i+3][j+3]:
                            coincidences += 1
                            # 'marco' las posiciones donde se encontro una diagonal para no iterar sobre ellas
                            pos.append([i,j])
                            pos.append([i+1,j+1])
                            pos.append([i+2,j+2])
                            pos.append([i+3,j+3])
    # de abajo a arriba e izquierda a derecha
    pos=[]
    for i in range(5,2,-1):
        for j in range(3):
            if [i,j] not in pos:
                letter = dna[i][j]
                if letter == dna[i-1][j+1]:
                    if letter == dna[i-2][j+2]:
                        if letter == dna[i-3][j+3]:
                            coincidences += 1
                            pos.append([i,j])
                            pos.append([i-1,j+1])
                            pos.append([i-2,j+2])
                            pos.append([i-3,j+3])
    return coincidences






# FUNCION LLENAR LA SECUENCIA DE ADN
def fill_dna_secuence (dna):
    print()
    print("Ingrese las letras que componen la secuencia de 'ADN' ('A', 'C', 'G' o 'T'):")
    print()
    for r in range(6):
        print()
        for c in range(6):
            exit = False
            while exit == False:
                # letter = random.choice('ATCG') # LLENAR INSTANTANTEAMENTE DE FORMA ALEATORIA #
                letter    = input(f" posicion({r},{c}): ")
                dna[r][c] = letter
                exit      = letter_is_correct(letter, exit)
                if exit == True:
                    dna[r][c] = letter
                    break
    return dna






# FUNCION VERIFICAR QUE LA LETRA INGRESADA SEA CORRECTA
def letter_is_correct(letter, exit):
    if letter=='A' or letter=='G' or letter=='T' or letter=='C':
        exit = True
    else:
        print("Letra incorrecta. Inrgese una letra correcta")
        exit = False
    return exit