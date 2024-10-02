n = int(input())
lista_numeros = []
n = int(input())
base = 0
teste = 0
while base < n:
    x = int(input())
    lista_numeros.append(x)
    base = base + 1
for i in range(n):
    if (lista_numeros[i] == 0):
        print("NULL")
    else:
        if lista_numeros[i]%2 == 0:
            if lista_numeros[i] < 0:
                print("EVEN NEGATIVE")
            else:
                print("EVEN POSITIVE")
        else:
            if lista_numeros[i] < 0:
                print("ODD NEGATIVE")
            else:
                print("ODD POSITIVE")
    i = i+1