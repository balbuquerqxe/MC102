for j in range (10000000000):
    entrada = input().split()
    if entrada == ["0", "0"]:
        break
    novo_valor = []
    resposta = entrada[1]
    for i in range (0, len(entrada[1])):
        while entrada[0] == entrada[1][i]:
            novo_valor = entrada[1].replace(entrada[0], "")
            resposta = novo_valor
            break
    for i in range (0, len(novo_valor)-1):
        if novo_valor[i] == novo_valor[i+1] == "0" and entrada [0] != "0":
            resposta = novo_valor.replace(novo_valor[i], "")
    if resposta == "":
        print("0")
    else: 
        print(resposta)