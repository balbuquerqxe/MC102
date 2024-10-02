identificador = ['W', 'H', 'Q', 'E', 'S', 'T', 'X']
duracao = [1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64]
notas = dict(zip(identificador,duracao))

while True:
    duracao_nota = input().split("/") #Será inserida a partitura.
    if duracao_nota == ['*']: #Isso trará um fim ao código.
        break
    else:
        lista_tempo_composicao = []
        quantidade_correta = 0
        for i in range (len(duracao_nota)):
            soma_compasso = 0
            for j in range (len(duracao_nota[i])):
                soma_compasso = notas[duracao_nota[i][j]] + soma_compasso #Soma que terá que dar 1 para estar certo
            lista_tempo_composicao.append(soma_compasso)
        for k in lista_tempo_composicao:
            if k == 1:
                quantidade_correta = quantidade_correta + 1 #Quantos compassos estão certos.
        print(quantidade_correta)