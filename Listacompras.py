n = int(input()) #Indica o número de linhas
for i in range (n):
    compras = input().split()
    sem_repeticao = sorted(set(compras))
    print(" ".join(sem_repeticao))