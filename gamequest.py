local = int(input())
if (local == 0):
    #Será físico
    companhia = int(input())
    if (companhia == 0):
        #Será com a família
        idade = int(input())
        if (idade == 0):
            print ("O Castelo é Nosso")
        elif (idade == 1):
            print ("Mysterium Park")
        elif (idade == 2):
            print ("Pandemic")
        else:
            print ("Qual é o Seu Meme?")
    elif (companhia == 1):
        #Será com a galera
        participantes = int(input())
        if (participantes == 0):
            print ("Descent: Lendas da Escuridão")
        elif (participantes == 1):
            print ("Dixit")
        elif (participantes == 2):
            print ("The Resistance")
        else:
            print ("Sim, Mestre das Trevas (Edição Verde)")
    elif (companhia == 2):
        #Será com crianças
        preco = int(input())
        if (preco == 0):
            print ("Dobble: Pixar")
        elif (preco == 1):
            print ("Caça aos Monstros")
        elif (preco == 2):
            print ("Ticket to Ride: Trem Fantasma")
        else:
            print ("Scooby-Doo: The Board Game")
    else:
        #Será à dois
        tempo = int(input())
        if (tempo == 0):
            print ("Exploding Kittens")
        elif (tempo == 1):
            print ("7 Wonders Duel")
        elif (tempo == 2):
            print ("Azul: Pavilhão de Verão")
        elif (tempo == 3):
            print ("Power Grid: Versão Energizada")
        else:
            print ("Star Wars Rebellion")
else:
    #Será virtual
    genero = int(input())
    if (genero == 0):
        #Será RPG
        rpg = int(input())
        if (rpg == 0):
            ano_lancamento = int(input())
            if (ano_lancamento == 0):
                print ("Valheim")
            elif (ano_lancamento == 1):
                print ("God of War")
            elif (ano_lancamento == 2):
                print ("Baldur's Gate 3")
            else:
                print ("Palworld")
        else:
            tematica = int(input())
            if (tematica == 0):
                print ("Horizon Forbidden West")
            elif (tematica == 1):
                print ("Hogwarts Legacy")
            else:
                print ("ELDEN RING")
    elif (genero == 1):
        #Será esporte
        categoria_esporte = int(input())
        if (categoria_esporte == 0):
            print ("Forza Horizon 4")
        elif (categoria_esporte == 1):
            print ("Session: Skate Sim")
        else:
            print ("FIFA 22")
    elif (genero == 2):
        #Será simulador
        tipo_simulador = int(input())
        if (tipo_simulador == 0):
            print ("Euro Truck Simulator 2")
        elif (tipo_simulador == 1):
            print ("Stardew Valley")
        elif (tipo_simulador == 2):
            print ("Kerbal Space Program")
        else:
            #Será jogo de vida real
            jogo_vida = int(input())
            if (jogo_vida == 0):
                print ("The Sims 1")
            elif (jogo_vida == 1):
                print ("The Sims 2")
            elif (jogo_vida == 2):
                print ("The Sims 3")
            else:
                #The Sims 4 expandido
                expansao = int(input())
                if (expansao == 0):
                    print ("Parenthood")
                elif (expansao == 1):
                    print ("Junte-se à Galera")
                elif (expansao == 2):
                    print ("Vida Campestre")
                elif (expansao == 3):
                    print ("A Aventura de Crescer")
                elif (expansao == 4):
                    print ("Vida Universitária")
                else:
                    print ("Cats & Dogs")
    else:
        avaliacao = int(input())
        if (avaliacao == 0):
            print ("Thronefall")
        elif (avaliacao == 1):
            print ("Orcs Must Die! 3")
        else:
            print ("Plants vs. Zombies")