
lista_sim = []   # Lista das pessoas que querem ser amigas.
lista_nao = []   # Lista das pessoas que não querem ser amigas.

while True:
    inscricao = input()   # Entrada.

    if inscricao == "FIM":   # Fim das inscrições.
        break

    inscricao = inscricao.split(" ")

    if inscricao [1] == "YES" and inscricao[0] not in lista_sim:   # Lista quem respondeu "YES".
        lista_sim.append(inscricao[0])
    elif inscricao [1] == "NO" and inscricao[0] not in lista_nao:   #Lista quem respondeu "NO".
        lista_nao.append(inscricao[0])

for nome in sorted(lista_sim):   # Ordena os nomes que responderam "YES" e os imprime.
    print (nome)

for nome in sorted(lista_nao):   # Ordena os nomes que responderam "NO" e os imprime.
    print (nome)

tamanho_nome = 0

for candidato in lista_sim:
    if len(candidato) > tamanho_nome:
        tamanho_nome = len(candidato)   # O primeiro critério é o candidato de maior nome.

for candidato in lista_sim:
    if len(candidato) == tamanho_nome:   # Se empatar, deve ser o que se inscreveu primeiro.
        print()
        print ("Amigo do Habay:")
        print (candidato)
        break
