n,k = input().split()   # Número de alunos, número sorteado.
nomes = []   # Lista com os nomes dos alunos.

for i in range (int(n)):
    nomes.append(input())
nomes_ordenados = sorted(nomes)   # Lista com os nomes dos alunos em ordem alfabética.
print(nomes_ordenados[int(k)-1])   #Imprime o aluno sorteado da lista ordenada.
