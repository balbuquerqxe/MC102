n = int(input())   # Número de países participantes.
lista_ordem_mudada = []   # Lista os países de acordo com a sua quantidade de medalhas de ouro, prata e bronze.
lista_informacao_paises = []   # Lista os países em ordem alfabética.

for i in range (n):   # Adiciona os países nas listas.
    pais, ouro, prata, bronze = input().split()   # Informação de cada país.
    lista_informacao_paises.append([pais, int(ouro), int(prata), int(bronze)])

lista_informacao_paises.sort(key = lambda x: (-x[1], -x[2], - x[3], x[0]))   # Ordena, primeiramente, em ordem decrescente das medalhas de ouro, prata e bronze; depois, em ordem alfabética os nomes.

for pais in lista_informacao_paises:
    print (pais[0], pais[1], pais[2], pais[3])   # Imprime cada um dos países.