while True:
    entrada = input().split()
    lista_possibilidades = []
    numero_servidor = []
    lista_conexoes_servidor = []
    quantidade = 0
    dicionario = {}
    if entrada == ['0', '0']:
        break
    for i in range (int(entrada[0])):
        servidor = input().split()
        servidor.remove(servidor[0])
        conexoes_fornecidas = set(servidor)
        dicionario[i] = conexoes_fornecidas
    for j in range (int(entrada[1])):
        cliente = set(input().split())
        interseccoes = set()
        for k in range(len(dicionario)):
            if cliente.intersection(dicionario[k]) != set():
                interseccoes.add(k)
        quantidade +=(len(interseccoes))
    print(quantidade)
