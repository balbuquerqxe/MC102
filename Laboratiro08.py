''' Primeira parte do programa: delimitar quais são as árvores que não podem ser vistas.
        1. Pedir as dimensões da área (matriz)
        2. Criar uma "nova matriz" eliminando a primeira linha e coluna e a última linha e coluna.
        3. Comparar o valor com os seus arredores.'''

linhas, colunas = input().split(",")  # Quantidade de linhas e colunas na matriz.
mapeamento_arvores = []

for _ in range (int(linhas)):   # Utiliza a quantidade de linhas.
    linha = []
    registro_linha = input()
    for _ in range (int(colunas)):   # Utiliza a quantidade de colunas.
        linha.append(int(registro_linha[_]))
    mapeamento_arvores.append(linha)   # Construção do mapa.

arvores_candidatas = []   # Quais árvores podem ser usadas como mirantes.

'''Agora que o mapeamento está pronto, precisamos comparar cada árvore com os seus arredores.'''

def em_cima (mapeamento_arvores, l, c):
    ''' Verifica as linhas em cima da árvore, que, se forem maiores, estarão escondendo o mirante.'''   
    for x in range (l):   
        if mapeamento_arvores[x][c] >= mapeamento_arvores[l][c]:
            return True
    
def embaixo (mapeamento_arvores, l, c):
    ''' Verifica as linhas embaixo da árvore, que, se forem maiores, estarão escondendo o mirante.'''   
    for x in range (l+1, int(linhas)):
        if mapeamento_arvores[x][c] >= mapeamento_arvores[l][c]:
            return True

def lado_esquerdo (mapeamento_arvores, l, c):
    ''' Verifica as colunas do lado esquerdo da árvore, que, se forem maiores, estarão escondendo o mirante.'''   
    for x in range (c):
        if mapeamento_arvores[l][x] >= mapeamento_arvores[l][c]:
            return True

def lado_direito (mapeamento_arvores, l, c):
    ''' Verifica as colunas do lado direito da árvore, que, se forem maiores, estarão escondendo o mirante.'''   
    for x in range (c+1, int(colunas)):
        if mapeamento_arvores[l][x] >= mapeamento_arvores[l][c]:
            return True

print("Árvores candidatas:")
for l in range (1, int(linhas)-1):   #Utiliza a quantidade de linhas.
    for c in range (1, int(colunas)-1):   #Utiliza a quantidade de colunas.
        if em_cima(mapeamento_arvores, l, c) == True and embaixo(mapeamento_arvores, l, c) == True and lado_esquerdo(mapeamento_arvores, l, c) == True and lado_direito(mapeamento_arvores, l, c) == True:
            print(f"{l},{c}")
            arvores_candidatas.append(f"{l},{c}")

'''Segunda parte do programa: dentre as árvores candidatas, escolher a que tem menos árvores bloquando a vista.
    1. Melhor vista = ver uma maior quantidade de árvores.
    2. É necessário comparar a quantidade de árvores que cada candidata consegue observar.
    3. Considerar lados e diagnais.'''

def arvores_em_cima (linha_selecionada, coluna_selecionada):
    ''' Conta a quantidade de árvores em cima do possível mirante.'''   

    quantidade = 0

    for linha_em_cima in range (linha_selecionada-1, -1, -1):
        if mapeamento_arvores[linha_em_cima][coluna_selecionada] < mapeamento_arvores[linha_selecionada][coluna_selecionada]:
            quantidade += 1   # Se a árvore for menor, ela será vista.
        else:
            quantidade += 1   #Se ela for maior ou igual, também será vista; porém, bloquará as que estão depois dela, parando a contagem.
            return quantidade
    quantidade =+1
    return quantidade

def arvores_embaixo(linha_selecionada, coluna_selecionada, total_linhas):
    ''' Conta a quantidade de árvores embaixo do possível mirante.'''   

    quantidade = 0

    for linha_embaixo in range (linha_selecionada+1, total_linhas+1):
        if mapeamento_arvores[linha_embaixo][coluna_selecionada] < mapeamento_arvores[linha_selecionada][coluna_selecionada]:
            quantidade += 1   # Se a árvore for menor, ela será vista.
        else:
            quantidade += 1   #Se ela for maior ou igual, também será vista; porém, bloquará as que estão depois dela, parando a contagem.
            return quantidade
    quantidade =+1
    return quantidade
    
def arvores_lado_esquerdo(linha_selecionada, coluna_selecionada):
    ''' Conta a quantidade de árvores do lado esqurdo do possível mirante.'''   

    quantidade = 0
    
    for coluna_esquerda in range (coluna_selecionada-1, -11, -1):
        if mapeamento_arvores[linha_selecionada][coluna_esquerda] < mapeamento_arvores[linha_selecionada][coluna_selecionada]:
            quantidade += 1   # Se a árvore for menor, ela será vista.
        else:
            quantidade += 1   #Se ela for maior ou igual, também será vista; porém, bloquará as que estão depois dela, parando a contagem.
            return quantidade
    quantidade = + 1
    return quantidade

def arvores_lado_direito(linha_selecionada, coluna_selecionada, total_colunas):
    ''' Conta a quantidade de árvores do lado direito do possível mirante.'''   

    quantidade = 0
    
    for coluna_direita in range (coluna_selecionada+1, total_colunas+1):
        if mapeamento_arvores[linha_selecionada][coluna_direita] < mapeamento_arvores[linha_selecionada][coluna_selecionada]:
            quantidade += 1   # Se a árvore for menor, ela será vista.
        else:
            quantidade += 1
            return quantidade   #Se ela for maior ou igual, também será vista; porém, bloquará as que estão depois dela, parando a contagem.
    quantidade +=1
    return quantidade            

def arvores_diagonal_1_quadrante (linha_selecionada, coluna_selecionada, total_colunas):
    ''' Conta a quantidade de árvores da diagonal do primeiro quadrante do possível mirante.'''   

    quantidade = 0
    coluna_direita = coluna_selecionada + 1   # Como vai no sentido da contagem de colunas, o número cresce.
    linha_em_cima = linha_selecionada - 1   # Como vai no sentido contrário da contagem de linhas, o número diminui.

    while coluna_direita < total_colunas-1 and linha_em_cima > 0:
        if mapeamento_arvores[linha_em_cima][coluna_direita] < mapeamento_arvores[linha_selecionada][coluna_selecionada]:
            quantidade += 1
        else:
            quantidade += 1
            return quantidade
        coluna_direita +=1
        linha_em_cima -=1
    quantidade +=1
    return quantidade        

def arvores_diagonal_2_quadrante (linha_selecionada, coluna_selecionada):
    ''' Conta a quantidade de árvores da diagonal do segundo quadrante do possível mirante.'''       

    quantidade = 0
    coluna_esquerda = coluna_selecionada -1   # Como vai no sentido contrário da contagem de colunas, o número diminui.
    linha_em_cima = linha_selecionada - 1   # Como vai no sentido contrário da contagem de linhas, o número diminui.

    while coluna_esquerda > 0 and linha_em_cima > 0:
        if mapeamento_arvores[linha_em_cima][coluna_esquerda] < mapeamento_arvores[linha_selecionada][coluna_selecionada]:
            quantidade += 1
        else:
            quantidade += 1
            return quantidade
        coluna_esquerda -=1
        linha_em_cima -=1
    quantidade +=1
    return quantidade  

def arvores_diagonal_3_quadrante (linha_selecionada, coluna_selecionada, total_linhas):
    ''' Conta a quantidade de árvores da diagonal do terceiro quadrante do possível mirante.'''   
    
    quantidade = 0
    coluna_esquerda = coluna_selecionada - 1   # Como vai no sentido contrário da contagem de colunas, o número diminui.
    linha_embaixo = linha_selecionada + 1   # Como vai no sentido da contagem de linhas, o número cresce.

    while coluna_esquerda > 0 and linha_embaixo < total_linhas-1:
        if mapeamento_arvores[linha_embaixo][coluna_esquerda] < mapeamento_arvores[linha_selecionada][coluna_selecionada]:
            quantidade += 1
        else:
            quantidade += 1
            return quantidade
        coluna_esquerda -=1
        linha_embaixo +=1
    quantidade +=1
    return quantidade  

def arvores_diagonal_4_quadrante (linha_selecionada, coluna_selecionada, total_linhas, total_colunas):
    ''' Conta a quantidade de árvores da diagonal do quarto quadrante do possível mirante.'''   

    quantidade = 0
    coluna_direita = coluna_selecionada + 1   # Como vai no sentido da contagem de colunas, o número cresce.
    linha_embaixo = linha_selecionada + 1   # Como vai no sentido da contagem de linhas, o número cresce.

    while coluna_direita < total_colunas-1 and linha_embaixo < total_linhas-1:
        if mapeamento_arvores[linha_embaixo][coluna_direita] < mapeamento_arvores[linha_selecionada][coluna_selecionada]:
            quantidade += 1
        else:
            quantidade += 1
            return quantidade
        coluna_direita +=1
        linha_embaixo +=1
    quantidade +=1
    return quantidade  

quantidade_vista = []   #Anexará a quantidade de árvores vistas por cada possível mirante.
for arvore in arvores_candidatas:   #Registrará a quantidade de árvores vistas de cada mirante.
    linha_selecionada = int(arvore[0])
    coluna_selecionada = int (arvore[2])
    quantidade_vista.append(arvores_em_cima (linha_selecionada, coluna_selecionada) + arvores_embaixo(linha_selecionada, coluna_selecionada, int(linhas)) + arvores_lado_esquerdo(linha_selecionada, coluna_selecionada) + arvores_lado_direito(linha_selecionada, coluna_selecionada, int(colunas)) + arvores_diagonal_1_quadrante(linha_selecionada, coluna_selecionada, int(colunas)) + arvores_diagonal_2_quadrante (linha_selecionada, coluna_selecionada) + arvores_diagonal_3_quadrante(linha_selecionada, coluna_selecionada, int(linhas)) + arvores_diagonal_4_quadrante(linha_selecionada, coluna_selecionada, int(linhas), int(colunas)))

melhor_arvore = 0 
for i in range(1,len(quantidade_vista)):   # Comparação entre as possíveis árvores para descobrir a que tem uma vista mais ampla.
    if quantidade_vista[i] > quantidade_vista[melhor_arvore]:
        melhor_arvore = i

print("Árvore escolhida:")
print(f"{arvores_candidatas[melhor_arvore]} com {quantidade_vista[melhor_arvore]} árvores visíveis.")