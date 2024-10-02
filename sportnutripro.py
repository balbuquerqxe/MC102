N = int(input())
lista_alimentos = []

for i in range(N):
    lista_alimentos.append(input().split())

M = int(input())

for j in range(M):
    ProteinPackets = 0
    CodeCarbs = 0
    DataLipids = 0
    atleta = input().split()
    for l in range(3):
        refeicao = input().split()
        for comida in refeicao:
            for alimento in lista_alimentos:
                if comida == alimento[0]:
                    ProteinPackets += float(alimento[1])
                    CodeCarbs += float(alimento[2])
                    DataLipids += float(alimento[3])

    diferenca_proteina = float(atleta[1]) - ProteinPackets
    diferenca_carboidrato = float(atleta[2]) - CodeCarbs
    diferenca_lipidios = float(atleta[3]) - DataLipids
    
    print(atleta[0])

    if diferenca_proteina < 0:
        print(-diferenca_proteina, "gramas de ProteinPackets em excesso")
    elif diferenca_proteina > 0:
        print(diferenca_proteina, "gramas de ProteinPackets em falta")
    else:
        print (ProteinPackets, "gramas de ProteinPackets adequado")

    if diferenca_carboidrato < 0:
        print(-diferenca_carboidrato, "gramas de CodeCarbs em excesso")
    elif diferenca_carboidrato > 0:
        print(diferenca_carboidrato, "gramas de CodeCarbs em falta")
    else:
        print (CodeCarbs, "gramas de CodeCarbs adequado")

    if diferenca_lipidios < 0:
        print(-diferenca_lipidios, "gramas de DataLipids em excesso")
    elif diferenca_lipidios > 0:
        print(diferenca_lipidios, "gramas de DataLipids em falta")
    else:
        print (DataLipids, "gramas de DataLipids adequado")