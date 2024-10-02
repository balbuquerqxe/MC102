T = int(input())
casos = []
for i in range (T):
    casos.append(str(input()))
for i in range (T):
    valores = casos[i].split(" ")
    PA = int(valores[0])
    PG = int(valores[1])
    G1 = float(valores[2])
    G2 = float(valores[3])
    anos = 0
    while (PA <= PG):
        PA = (PA*(1 + (G1/100)))//1
        PG = (PG * (1 + (G2/100)))//1
        anos = anos +1
        if (PA > PG) or (anos > 100):
            break
    if (anos > 100):
        print ("Mais de 1 seculo.")
    else:
        print (anos, "anos.")
        