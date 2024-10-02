#n será o valor inserido
n=int(input())
#quantidade de notas de 100 usadas
notas100=n//100 
resto1=n%100
if (resto1!=0):
    notas50=resto1//50
    resto2=resto1%50
if (resto2!=0):
    notas20=resto2//20
    resto3=resto2%20
if (resto3!=0):
    notas10=resto3//10
    resto4=resto3%10
if (resto4!=0):
    notas5=resto4//5
    resto5=resto4%5
if (resto5!=0):
    notas2=resto5//2
    resto6=resto5%2
print(n)
print(notas100, "nota(s) de R$ 100,00")
print(notas50, "nota(s) de R$ 50,00")
print(notas20, "nota(s) de R$ 20,00")
print(notas10, "nota(s) de R$ 10,00")
print(notas5, "nota(s) de R$ 5,00")
print(notas2, "nota(s) de R$ 2,00")
print(resto6, "nota(s) de R$ 1,00")

