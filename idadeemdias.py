n=int(input())
anos=n//365
resto=n%365
meses=resto//30
dias=resto%30
print(anos,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")