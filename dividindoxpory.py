n = int(input())
todos_pares = []
for i in range (n):
    conjunto = input()
    todos_pares.append(conjunto)
for j in range (n):
    conjunto_separado = todos_pares[j].split(" ")
    x = int (conjunto_separado[0])
    y = int (conjunto_separado[1])
    if y == 0:
        print ("divisao impossivel")
    else: 
        divisao = x/y
        print (f"{divisao:.1f}")