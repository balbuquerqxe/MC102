todas_mochilas = input()
mochila = todas_mochilas.split()
item_repetido = 0
for i in range (len(mochila)):
    total_de_itens = int(len(mochila[i]))
    cada_item = mochila[i]
    repetido = False
    for j in range (int(total_de_itens/2)):
        elemento_compartimento_1 = cada_item[j]
        for k in range (int(total_de_itens/2), int(total_de_itens)):
            elemento_compartimento_2 = cada_item[k]
            if elemento_compartimento_1 == elemento_compartimento_2:
                repetido = True
                item_repetido = elemento_compartimento_1
                break
            
    if repetido == True:
        print ("mochila ", i+1,": ", item_repetido, sep = "")
    else:
        print ("mochila ", i+1,": Sem item repetido", sep = "")