while True:
    try:

        n = int(input())   # Quantidade de livros.
        livros = []   # Lista com os códigos dos livros.

        for i in range (n):
            livros.append(input())
        livros_ordenados = sorted(livros)   # Livros ordenados.
        for livro in livros_ordenados:
            print (livro)   # Imprime cada um dos livros ordenados.
    
    except EOFError:   # Quando acabar o arquivo.
        break