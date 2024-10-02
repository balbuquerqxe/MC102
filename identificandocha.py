T = int(input())
respostas = input()
lista = respostas.split()
acertos = 0
for i in range (len(lista)):
    if int(lista[i]) == T:
        acertos = acertos + 1
print(acertos)