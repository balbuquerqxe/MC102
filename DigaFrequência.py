primeira_saida = True
while True:
    try:
        caso_teste = input()   # Insere os caracteres.

        if primeira_saida == False:   # Imprime a linha em branco entre os conjuntos.
            print ()
        
        primeira_saida = False
        
        dicionario = {}   # Registrará o valor ASCII do caracter e a sua frequência.
        for caracter in caso_teste:
            if -ord(caracter) not in dicionario:
                dicionario [-ord(caracter)] = 1   # O caracter apareceu pela primeira vez.
            else:
                dicionario[-ord(caracter)] += 1   # O caracter já apareceu anteriormente.
        
        valores = sorted(list(dicionario.values()))   # Ordena a frequência em ordem crescente.
        chaves = sorted(list(dicionario.keys()))   # Ordena os valores ASCII em ordem crescente.
        copia_valores = valores.copy()

        for k in range (1,len(valores)):
            if valores[k-1] == valores[k]:
                copia_valores.remove(valores[k-1])   # Remove os número repetidos de frequência.

        # Aqui será associado o valor de frequência com o número ASCII.
        for valor in copia_valores:
            for chave in chaves:
                if dicionario[chave] == valor:
                    print (-chave, valor)

    except EOFError:
        break