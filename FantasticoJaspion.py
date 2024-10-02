t = int(input())   #Número de instâncias
for i in range(t):
    dicionario = {}
    letra_traduzida = []
    m_n = input().split()   #Número de palavras e número de linhas da letra
    for j in range(int(m_n[0])):
        japones = input()
        portugues = input()
        dicionario[japones] = portugues
    for k in range(int(m_n[1])):
        linha_traduzida = []
        letra = input().split()
        for l in range(len(letra)):
            if letra[l] in dicionario:
                traducao = dicionario[letra[l]]
            else:
                traducao = letra[l]
            linha_traduzida.append(traducao)
        print(' '.join(linha_traduzida))
    print()