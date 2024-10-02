n = int(input())   # Número de casos teste.

for i in range (n):
    
    jantar = []   # Lista os alimentos, se houverem, do jantar.
    alimentos_dieta = input()   # Alimentos da dieta.
    cafe = input()   # O que foi consumido no café.
    almoco = input()   # O que foi consumido no jantar.
    
    for alimento in alimentos_dieta: 
        if alimento not in cafe and alimento not in almoco:   # Se o alimento não foi consumido ainda...
            jantar.append(alimento)   # ...ele deve ser consumido no jantar.
    resultado = "".join(sorted(jantar)) # Junção dos alimentos do jantar e sua organização em ordem alfabetica.
    
    for comida_almoco in almoco:
        if comida_almoco not in alimentos_dieta:   # Se um alimento não listado na dieta foi consumido.
            resultado = "CHEATER"
    
    for comida_cafe in cafe:
        if comida_cafe not in alimentos_dieta:   # Se um alimento não listado na dieta foi consumido.
            resultado = "CHEATER"
    
    print (resultado)

