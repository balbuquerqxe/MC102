n = int(input())   # Indica a quantidade de crianças.
nomes = []   # Lista com os nomes de todas as crianças.
positivo = 0   # Crianças que se comportaram bem.
negativo = 0   # Crianças que não se comportaram.

for i in range(n):
    comportamento, nome = input().split()
    nomes.append(nome)   # Lista todos os nomes.
    if comportamento == "+":
        positivo +=1   # Quantidade que se comportou bem.
    else:
        negativo +=1   # Quantidade que não se comportou bem.
nomes_ordenados = sorted(nomes)   # Coloca os nomes em ordem alfabética.
for nome in nomes_ordenados:
    print(nome)
print("Se comportaram:", positivo, "| Nao se comportaram:", negativo)
