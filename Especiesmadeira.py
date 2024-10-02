n = int(input()) #Indica o número de casos de teste.
linha_em_branco = input()
for i in range(n):
    dicionario_arvores = {} 
    quantidade_arvores = 0

    while True:   #Enquanto não tiver uma linha em branco, o conjunto é ainda o mesmo.
        try:
            entrada = input()
            if entrada == "":
                break
            else:
                if entrada not in dicionario_arvores:   #Primeira vez que aparece essa árvore.
                    arvore = {entrada: 1}
                else:
                    arvore = {entrada: dicionario_arvores[entrada] + 1}
                quantidade_arvores = quantidade_arvores + 1
                dicionario_arvores.update(arvore)
        except EOFError:
            break
    ordem_alfabetica = sorted(dicionario_arvores.items())   #Organiza em ordem alfabética

    for j in range (len(ordem_alfabetica)):
        porcentagem = ("{:.4f}".format((dicionario_arvores.get(ordem_alfabetica[j][0]))*100/quantidade_arvores))   #Coloca os valores em porcentagem
        print (ordem_alfabetica[j][0], porcentagem)
    if i < n - 1:
        print()


    