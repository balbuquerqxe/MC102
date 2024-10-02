n = int(input())
experimento = []
resultado = []
coelho = 0
rato = 0
sapo = 0
for i in range(n):
    quantia = str(input())
    experimento.append(quantia)
    resultado = experimento[i].split (" ")
    numero_cobaias = int(resultado[0])
    tipo_cobaia = resultado[1]
    if tipo_cobaia == "C":
        coelho = coelho + numero_cobaias
    elif tipo_cobaia == "R":
        rato = rato + numero_cobaias
    else:
        sapo = sapo + numero_cobaias
total = coelho + rato + sapo
print ("Total:", total,"cobaias")
print ("Total de coelhos:", coelho)
print ("Total de ratos:", rato)
print ("Total de sapos:", sapo)
print ("Percentual de coelhos:", f"{100*coelho/total:.2f}","%")
print ("Percentual de ratos:", f"{100*rato/total:.2f}","%")
print ("Percentual de sapos:", f"{100*sapo/total:.2f}", "%")