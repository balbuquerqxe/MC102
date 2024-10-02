primeira_saida = True   # Controla a linha em branco entre os conjuntos.

while True:
    n = int(input())   # Número de camisetas.
    lista_dados = []   # Armazenará todas as informações de todos os alunos.

    if n == 0:   # Se n = 0, o código não deve continuar.
        break

    for i in range(n):
        nome = input()
        cor, tamanho = input().split()
        lista_dados.append([nome, cor, tamanho])   # Lista anexará os dados de todos os alunos.
    lista_dados.sort(key = lambda x: (x[1], -ord(x[2]), x[0]))   # Ordenação a partir da cor, depois tamanho e depois pela ordem alfabética.

    if primeira_saida == False:   # Controla qual linha será pulada.
        print()   # Pula uma linha.

    primeira_saida = False
    
    for dado in lista_dados:
        print (dado[1], dado[2], dado[0])   # Juntando as informações para imprimir.
        
        