todas_mochilas = input()
mochila = todas_mochilas.split()
for i in range (len(mochila)):
    total_de_itens = int(len(mochila[i]))
    compartimento1 = int(total_de_itens/2)
    cada_item = list(mochila[i])
    j = 0
    houve_repetido = False
    while j < compartimento1:
        elemento_compartimento_1 = cada_item[j]
        p = compartimento1
        while (p < total_de_itens):
            elemento_compartimento_2 = cada_item[p]  
            while elemento_compartimento_1 == elemento_compartimento_2:
                p = total_de_itens
                j = compartimento1
                houve_repetido = True
                print ("mochila ", i+1,": ",elemento_compartimento_1, sep = "")
                break 
            else:
                p = p + 1
        j = j + 1
    if houve_repetido == False:
        print ("mochila ", i+1,": Sem item repetido", sep = "")