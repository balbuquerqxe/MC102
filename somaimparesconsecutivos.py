x = int(input())
y = int(input())
soma = 0
if (x == y):
    print(soma)
elif (x < y):
    if x%2 == 0:
        for numeroimpar in range (x-1,y,2):
            soma = soma + numeroimpar
        print(soma)
    else:
        for numeroimpar in range (x,y,2):
            soma = soma + numeroimpar - x
            print (soma)
else:
    if x%2 == 0:
        for numeroimpar in range (x-1,y,-2):
            soma = soma + numeroimpar
        print(soma)
    else:
        for numeroimpar in range (x,y,-2):
            soma = soma + numeroimpar
        print(soma-x)