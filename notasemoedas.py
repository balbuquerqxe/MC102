n=float(input())
notas100=n//100 
resto1=n%100
notas50=resto1//50
resto2=resto1%50
notas20=resto2//20
resto3=resto2%20
notas10=resto3//10
resto4=resto3%10
notas5=resto4//5
resto5=resto4%5
notas2=resto5//2
resto6=resto5%2
moedas1=resto6//1
resto7=resto6%1
moedas50=resto7//0.50
resto8=resto7%0.50
moedas25=resto8//0.25
resto9=resto8%0.25
moedas10=resto9//0.10
resto10=resto9%0.10
moedas05=resto10//0.05
resto11= resto10%0.05
moedas01=round(resto11/0.01,2)

#notas
print("NOTAS:")
print(int(notas100), "nota(s) de R$ 100.00")
print(int(notas50), "nota(s) de R$ 50.00")
print(int(notas20), "nota(s) de R$ 20.00")
print(int(notas10), "nota(s) de R$ 10.00")
print(int(notas5), "nota(s) de R$ 5.00")
print(int(notas2), "nota(s) de R$ 2.00")
#moedas
print("MOEDAS:")
print(int(moedas1), "moeda(s) de R$ 1.00")
print(int(moedas50), "moeda(s) de R$ 0.50")
print(int(moedas25), "moeda(s) de R$ 0.25")
print(int(moedas10), "moeda(s) de R$ 0.10")
print(int(moedas05), "moeda(s) de R$ 0.05")
print(int(moedas01), "moeda(s) de R$ 0.01")