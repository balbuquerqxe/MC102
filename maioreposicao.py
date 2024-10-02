lista_numeros = []
maior = 0
local = 0
while local < 100:
    numero = int(input())
    lista_numeros.append(numero)
    local = local +1
for posicao in range (100):
    if lista_numeros[posicao] > maior:
        maior = lista_numeros[posicao]
    else:
        maior = maior
print(maior)
print(lista_numeros.index(maior)+1)
