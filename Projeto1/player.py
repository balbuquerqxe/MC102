#!/usr/bin/env python3

from colors import *
from random import sample
from itertools import permutations
from itertools import combinations

# Cores disponíveis para o palpite
cores = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
todas_opcoes = permutations (cores,4)
lista_todos_casos = []
possibilidades_palpite = []

for um_dos_casos in todas_opcoes:
    caso = list(um_dos_casos)
    lista_todos_casos.append(caso)

opcoes_palpite = lista_todos_casos.copy()

def player(guess_hist, res_hist):
    if len(res_hist) < 1:
        global cores
        cores = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
        global opcoes_palpite
        opcoes_palpite = lista_todos_casos.copy()
        return sample (cores, 4)
        # Essa será a única vez que o palpite será verdadeiramente aleatório.    
    elif res_hist[-1][0] == 1:
        # Apenas uma cor está certa.
        return uma_certa (guess_hist, res_hist)
    elif res_hist[-1][0] == 2:
        # Apenas duas cores estão certa.
        return duas_certas (guess_hist, res_hist)
    elif res_hist[-1][0] == 3:
        # Apenas três cores estão certa.
        return tres_certas (guess_hist, res_hist)
    else:
        # Todas as cores estão certas.
        return todas_certas (guess_hist, res_hist)

def uma_certa (guess_hist, res_hist):
    '''Essa função trabalhará com os palpites que possuem apenas uma cor correta, a qual pode tanto estar na posição certa como na errada.'''
    global opcoes_palpite

    #Se apenas uma cor está certa, isso indica que as três cores fora do palpite são corretas.
    cores_certas = cores
    for i in range (4):
        if guess_hist[-1][i] in cores_certas:
            cores_certas.remove(guess_hist[-1][i])

    # Se as cores certas não estão em um palpite, ele, automaticamente, está incorreto.
    for l in range (len(lista_todos_casos)):
        for j in range(len(cores_certas)):
            if cores_certas[j] not in lista_todos_casos[l] and lista_todos_casos[l] in opcoes_palpite:
                opcoes_palpite.remove(lista_todos_casos[l])
    
    for k in range (len(guess_hist)):
        if guess_hist[k] in opcoes_palpite:
            opcoes_palpite.remove(guess_hist[k])

    copia_opcoes_palpite = opcoes_palpite.copy()            

    if res_hist [-1][1] == 0:
    #Nenhuma cor do palpite estava na posição certa; logo, não vale a pena realizar um novo chute com ela no mesmo lugar.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][1] == copia_opcoes_palpite[i][1]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][2] == copia_opcoes_palpite[i][2]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
        palpite = sample (opcoes_palpite, 1)[0]
        return(palpite)
    if res_hist [-1][1] == 1:
     #A única cor certa nesse palpite também estava na posição certa; logo, não vale a pena realizar um novo chute com ela em um lugar diferente.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] in copia_opcoes_palpite[i] and guess_hist[-1][0] != copia_opcoes_palpite[i][0]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][1] in copia_opcoes_palpite[i] and guess_hist[-1][1] != copia_opcoes_palpite[i][1]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][2] in copia_opcoes_palpite[i] and guess_hist[-1][2] != copia_opcoes_palpite[i][2]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][3] in copia_opcoes_palpite[i] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
    
    palpite = sample (opcoes_palpite, 1)[0]
    return(palpite)

def duas_certas (guess_hist, res_hist):
    '''Essa função trabalhará com os palpites que possuem apenas duas cores corretas, as quais podem tanto estar na posição certa como na errada.'''
    global opcoes_palpite
    ultimo_palpite = guess_hist[-1]
    possibilidades_palpite = []

    #Se apenas duas cores estão certas, mas não sabemos quais, devemos realizar grupos das possíveis duplas de cores que podem estar certas.
    conjunto_cores = combinations (ultimo_palpite, 2)
    lista_todos_conjuntos = []

    for um_dos_casos in conjunto_cores:
        caso = list(um_dos_casos)
        lista_todos_conjuntos.append(caso)

    #Se a dupla de cores possivelmente certas estiver em um palpite, significa que ele pode estar correto.
    for l in range (len(lista_todos_casos)):
        if lista_todos_casos [l] in opcoes_palpite:
            for i in range (len(lista_todos_conjuntos)):
                if lista_todos_conjuntos[i][0] in lista_todos_casos[l] and lista_todos_conjuntos[i][1] in lista_todos_casos[l]:       
                        possibilidades_palpite.append(lista_todos_casos[l])

    #Se um palpite já foi feito anteriormente, isso significa que ele estava incorreto.
    for k in range (len(guess_hist)):
        if guess_hist[k] in opcoes_palpite:
            opcoes_palpite.remove(guess_hist[k])
    
    #Devemos realizar uma intersecção entre as opções para reduzir a quantidade de palpites.
    copia_opcoes_palpite = opcoes_palpite.copy()
    opcoes_palpite = []           

    for i in range (len(copia_opcoes_palpite)):
        if copia_opcoes_palpite[i] in possibilidades_palpite:
            opcoes_palpite.append(copia_opcoes_palpite[i])
    
    copia_opcoes_palpite = opcoes_palpite.copy()            

    if res_hist [-1][1] == 0:
    #Nenhuma cor do palpite estava na posição certa; logo, não vale a pena realizar um novo chute com ela no mesmo lugar.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][1] == copia_opcoes_palpite[i][1]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][2] == copia_opcoes_palpite[i][2]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
        palpite = sample (opcoes_palpite, 1)[0]
        return(palpite)
    
    elif res_hist [-1][1] == 1:
        possibilidades_palpite = []
    # Apenas uma cor do palpite estava na posição certa; logo, essa mesma condição deve ser mantida.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])

    elif res_hist [-1][1] == 2:
        possibilidades_palpite = []
    # Apenas duas cores do palpite estavam na posição certa; logo, essa mesma condição deve ser mantida.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])

    #Devemos realizar uma intersecção entre as opções para reduzir a quantidade de palpites.
    copia_opcoes_palpite = opcoes_palpite.copy()
    opcoes_palpite = []           

    for i in range (len(copia_opcoes_palpite)):
        if copia_opcoes_palpite[i] in possibilidades_palpite:
            opcoes_palpite.append(copia_opcoes_palpite[i])
       
    palpite = sample (opcoes_palpite, 1)[0]
    return(palpite)                   

def tres_certas (guess_hist, res_hist):
    '''Essa função trabalhará com os palpites que possuem apenas três cores corretas, as quais podem tanto estar na posição certa como na errada.'''
    global opcoes_palpite
    ultimo_palpite = guess_hist[-1]
    possibilidades_palpite = []

    #Se apenas três cores estão certas, mas não sabemos quais, devemos realizar grupos dos possíveis trios de cores que podem estar certas.
    conjunto_cores = combinations (ultimo_palpite, 3)
    lista_todos_conjuntos = []
    possibilidades_palpite = []

    for um_dos_casos in conjunto_cores:
        caso = list(um_dos_casos)
        lista_todos_conjuntos.append(caso)

    #Se o trio de cores possivelmente certas estiver em um palpite, significa que ele pode estar correto.
    for l in range (len(lista_todos_casos)):
        if lista_todos_casos [l] in opcoes_palpite:
            for i in range (len(lista_todos_conjuntos)):
                if lista_todos_conjuntos[i][0] in lista_todos_casos[l] and lista_todos_conjuntos[i][1] in lista_todos_casos[l] and lista_todos_conjuntos[i][2] in lista_todos_casos[l]:       
                        possibilidades_palpite.append(lista_todos_casos[l])

 #Se um palpite já foi feito anteriormente, isso significa que ele estava incorreto.
    for k in range (len(guess_hist)):
        if guess_hist[k] in opcoes_palpite:
            opcoes_palpite.remove(guess_hist[k])
    
    #Devemos realizar uma intersecção entre as opções para reduzir a quantidade de palpites.
    copia_opcoes_palpite = opcoes_palpite.copy()
    opcoes_palpite = []           

    for i in range (len(copia_opcoes_palpite)):
        if copia_opcoes_palpite[i] in possibilidades_palpite:
            opcoes_palpite.append(copia_opcoes_palpite[i])
    
    copia_opcoes_palpite = opcoes_palpite.copy()           

    if res_hist [-1][1] == 0:
    #Nenhuma cor do palpite estava na posição certa; logo, não vale a pena realizar um novo chute com ela no mesmo lugar.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][1] == copia_opcoes_palpite[i][1]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][2] == copia_opcoes_palpite[i][2]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
        palpite = sample (opcoes_palpite, 1)[0]
        return(palpite)
    
    elif res_hist [-1][1] == 1:
        possibilidades_palpite = []
    # Apenas uma cor do palpite estava na posição certa; logo, essa mesma condição deve ser mantida.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])

    elif res_hist [-1][1] == 2:
        possibilidades_palpite = []
    # Apenas duas cores do palpite estavam na posição certa; logo, essa mesma condição deve ser mantida.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
    elif res_hist [-1][1] == 3:
        possibilidades_palpite = []
    # Apenas três cores do palpite estavam na posição certa; logo, essa mesma condição deve ser mantida.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
    
    #Devemos realizar uma intersecção entre as opções para reduzir a quantidade de palpites.
    copia_opcoes_palpite = opcoes_palpite.copy()
    opcoes_palpite = []           

    for i in range (len(copia_opcoes_palpite)):
        if copia_opcoes_palpite[i] in possibilidades_palpite:
            opcoes_palpite.append(copia_opcoes_palpite[i])
       
    palpite = sample (opcoes_palpite, 1)[0]
    return(palpite)                                    

def todas_certas (guess_hist, res_hist):
    '''Essa função trabalhará com os palpites que possuem todas as cores corretas, restando, dessarte, descobrir as suas devidas posições.'''
    global opcoes_palpite
    cores_certas = guess_hist[-1].copy()
    possibilidades_palpite = []

    #Todas as cores do palpite anterior estavam certas e, por isso, devem aparecer em todos os palpites possíveis.
    
    for l in range(len(lista_todos_casos)):
        for j in range (len(cores_certas)):
            if cores_certas[j] not in lista_todos_casos[l] and lista_todos_casos[l] in opcoes_palpite:
                opcoes_palpite.remove(lista_todos_casos[l])
    
    for k in range (len(guess_hist)):
        if guess_hist[k] in opcoes_palpite:
            opcoes_palpite.remove(guess_hist[k])

    copia_opcoes_palpite = opcoes_palpite.copy()        
           
    if res_hist [-1][1] == 0:
    #Nenhuma cor do palpite estava na posição certa; logo, não vale a pena realizar um novo chute com ela no mesmo lugar.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][1] == copia_opcoes_palpite[i][1]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][2] == copia_opcoes_palpite[i][2]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
                elif guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    opcoes_palpite.remove(copia_opcoes_palpite[i])
        palpite = sample (opcoes_palpite, 1)[0]
        return(palpite)
    
    elif res_hist [-1][1] == 1:
        possibilidades_palpite = []
    # Apenas uma cor do palpite estava na posição certa; logo, essa mesma condição deve ser mantida.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])

    elif res_hist [-1][1] == 2:
        possibilidades_palpite = []
    # Apenas duas cores do palpite estavam na posição certa; logo, essa mesma condição deve ser mantida.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
    elif res_hist [-1][1] == 3:
        possibilidades_palpite = []
    # Apenas três cores do palpite estavam na posição certa; logo, essa mesma condição deve ser mantida.
        for i in range (len(copia_opcoes_palpite)):
            if copia_opcoes_palpite[i] in opcoes_palpite:
                if guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] != copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] != copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] == copia_opcoes_palpite[i][0] and guess_hist[-1][1] != copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
                elif guess_hist[-1][0] != copia_opcoes_palpite[i][0] and guess_hist[-1][1] == copia_opcoes_palpite[i][1] and guess_hist[-1][2] == copia_opcoes_palpite[i][2] and guess_hist[-1][3] == copia_opcoes_palpite[i][3]:
                    possibilidades_palpite.append(copia_opcoes_palpite[i])
    
    #Devemos realizar uma intersecção entre as opções para reduzir a quantidade de palpites.
    copia_opcoes_palpite = opcoes_palpite.copy()
    opcoes_palpite = []           

    for i in range (len(copia_opcoes_palpite)):
        if copia_opcoes_palpite[i] in possibilidades_palpite:
            opcoes_palpite.append(copia_opcoes_palpite[i])
       
    palpite = sample (opcoes_palpite, 1)[0]
    return(palpite)                              