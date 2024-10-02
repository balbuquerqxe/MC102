while True:
    try:

        n,q = input().split()   # Número de habitantes, número de consultas.
        notas = []

        for i in range(int(n)):
            notas.append(int(input()))   # Adiciona na lista cada uma das notas.

        notas_ordenadas = sorted(notas)   # Ordena as notas em ordem crescente.

        for j in range(int(q)):
            print(notas_ordenadas[-int(input())])   # Imprime as notas; como está ordenado no sentido crescente, o sinal de menos torna-se necessário.
    
    except EOFError:   # Quando o arquivo chega ao seu fim.
        break