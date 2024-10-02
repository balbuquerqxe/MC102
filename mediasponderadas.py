n = int(input())
todos_numeros = []
base = 0
lista_conjunto= 0
for base in range(n):
    x = str(input())
    todos_numeros.append(x)
    base = base + 1
for i in range(n):
    lista_conjunto = todos_numeros[i].split(" ")
    valor1 = float (lista_conjunto[0])
    valor2 = float (lista_conjunto[1])
    valor3 = float (lista_conjunto[2])
    media_ponderada = (valor1*2 + valor2*3 + valor3*5)/10
    print(f"{media_ponderada:.1f}")