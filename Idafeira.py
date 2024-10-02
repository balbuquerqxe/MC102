n = int(input()) #Indica a quantidade de idas à feira

for i in range(n):
    lista_produtos_disponiveis = []
    lista_precos = []
    lista_produtos_comprados = []
    lista_quantidades = []
    valor = 0.0
    m = int(input()) #Quantidade de produtos disponíveis na feira
    for j in range(m):
        produto_preco = input().split()
        lista_produtos_disponiveis.append(produto_preco[0])
        lista_precos.append(float(produto_preco[1]))
        dic_produto_preco = dict(zip(lista_produtos_disponiveis, lista_precos))
    p = int(input()) #Quantidade de produtos que serão comprados
    for k in range (p):
        produto_quantidade = input().split()
        lista_produtos_comprados.append(produto_quantidade[0])
        lista_quantidades.append(float(produto_quantidade[1]))
        dic_produto_quantidade = dict(zip(lista_produtos_comprados, lista_quantidades))
    for disponivel in lista_produtos_disponiveis: #A partir disso, será possível associar o valor do produto e a sua quantidade comprada
        if disponivel in lista_produtos_comprados:
            preco = dic_produto_preco[disponivel]*dic_produto_quantidade[disponivel]
            valor = valor + preco
    print ("R$", "{:.2f}".format(valor))

