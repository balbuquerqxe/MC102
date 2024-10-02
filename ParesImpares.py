n = int(input())   # Número de linhas.
pares = []   # Lista dos números pares.
impares = []   # Lista dos números ímpares.

for i in range (n):
    
    numero = int(input())
    
    if numero % 2 == 0:   # Isso indica que ele é par.
        pares.append(numero)
    
    else:   # Isso indica que ele é ímpar.
        impares.append(numero)

for par in sorted(pares):
    print(par)   # Ordem crescente.

for impar in sorted(impares, reverse = True):
    print (impar)   # O reverse é importante para imprimir na ordem decrescente.