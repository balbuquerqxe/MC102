lista = []
entrada = str(input())
lista.append(entrada)
incognitas = lista[0].split(" ")
x = int(incognitas[0])
y = int (incognitas[1])
ultimo_numero = 1
i = 1
while (i < x + 1):
    if (ultimo_numero > y):
        break
    print (ultimo_numero, end = "")
    ultimo_numero = ultimo_numero + 1
    i = i +1
    if (i >= x + 1):
        print ()
        i = 1
    else:
        print (end = " ")
        