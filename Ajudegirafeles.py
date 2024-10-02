while True:
    dicionario = {}
    erros = 0
    n = int(input())   #Representa a quantidade de alunos da turma
    if n == 0:
        break
    for i in range(n):
        modelo = input().split()
        dicionario[modelo[0]] = modelo[1]   #Correspondência entre nome e assinatura.
    m = int(input())
    for j in range(m):
        chamada = input().split()
        caracter_errado = 0   #Só será falsa se tiver 2 ou mais caracteres errados.
        for k in range(len(chamada[1])):
            if chamada[1][k] != dicionario[chamada[0]][k]:
                caracter_errado +=1
        if caracter_errado > 1:
            erros +=1 #Se for falsa, será contabilizado.
    print(erros)
