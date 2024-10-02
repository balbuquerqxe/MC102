caracteres_possiveis = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
lista_caracteres = []
lista_numeracao = []
for i in caracteres_possiveis:
    lista_caracteres.append(i)
    lista_numeracao.append(lista_caracteres.index(i))
dicionario = dict(zip(lista_caracteres, lista_numeracao))

def is_valid_key (key):
    '''Essa função irá indicar se a chave é válida ou não.'''
    if len(key) == 5:
        for i in range(5):
            if key[i] not in caracteres_possiveis:
                #A chave deve possuir apenas caracteres de intervalos específicos dos valores de ascii.
                return False
        return True
    else:
        return False

def is_inverse (public_key, private_key):
    '''Essa função verifica se uma chave é inversa da outra.'''
    if public_key == private_key[::-1]:
        return True
    else:
        return False

def inverse (message):
    '''Essa função inverte a mensagem'''
    return message[::-1]

def find_shifts (public_key, private_key):
    '''Essa função verifica se o tipo de criptografia usado será o fixo, ou seja, todos os shifts são iguais.'''
    valores_deslocamento = []
    for i in range (5):
        if dicionario[private_key[i]]-dicionario[public_key[i]] > 26:
            valores_deslocamento.append(dicionario[private_key[i]]-dicionario[public_key[i]] - 62)
        elif dicionario[private_key[i]]-dicionario[public_key[i]] < -26 :
            valores_deslocamento.append((dicionario[private_key[i]]-dicionario[public_key[i]]) + 62)
        else:
            valores_deslocamento.append(dicionario[private_key[i]]-dicionario[public_key[i]])
    if valores_deslocamento[0] == valores_deslocamento[1] == valores_deslocamento[2] == valores_deslocamento[3] == valores_deslocamento[4]:
        return valores_deslocamento[0]

def find_shifts_alternate (public_key, private_key):
    '''Essa função verifica se o tipo de criptografia usado será o alternado, ou seja, quando um shift é positivo e o outro negativo, seguindo um padrão.'''
    valores_deslocamento = []
    for i in range (5):
        if dicionario[private_key[i]]-dicionario[public_key[i]] > 26:
            valores_deslocamento.append(dicionario[private_key[i]]-dicionario[public_key[i]] - 62)
        elif dicionario[private_key[i]]-dicionario[public_key[i]] < -26 :
            valores_deslocamento.append((dicionario[private_key[i]]-dicionario[public_key[i]]) + 62)
        else:
            valores_deslocamento.append(dicionario[private_key[i]]-dicionario[public_key[i]])

    if valores_deslocamento[0] == - valores_deslocamento[1] == valores_deslocamento[2] == - valores_deslocamento[3] == valores_deslocamento[4]:     
        return valores_deslocamento[0]
    
def find_variable_shifts (public_key, private_key):
    '''Essa função verifica se o tipo de criptografia usado será o variável, ou seja, sem seguir um padrão.'''
    valores_deslocamento = []
    for i in range (5):
        if dicionario[private_key[i]]-dicionario[public_key[i]] > 26:
            valores_deslocamento.append(dicionario[private_key[i]]-dicionario[public_key[i]] - 62)
        elif dicionario[private_key[i]]-dicionario[public_key[i]] < -26 :
            valores_deslocamento.append((dicionario[private_key[i]]-dicionario[public_key[i]]) + 62)
        else:
            valores_deslocamento.append(dicionario[private_key[i]]-dicionario[public_key[i]])
    return valores_deslocamento

def shift_encrypt (shifts, message):
    '''Essa função cria a nova mensagem a partir do tipo fixo.'''
    novos_caracteres = []
    if shifts > 0:
        for i in range (len(message)):
            novo_valor = dicionario[message[i]] + shifts
            while novo_valor >= 62:
                novo_valor = novo_valor - 62
            novos_caracteres.append(caracteres_possiveis[novo_valor])
    else:
        for i in range (len(message)):
            novo_valor = dicionario[message[i]] + shifts
            while novo_valor < 0:
                novo_valor = novo_valor + 62
            novos_caracteres.append(caracteres_possiveis[novo_valor])  
    mensagem_criptografada = "".join(novos_caracteres)
    return mensagem_criptografada

def shift_alternate_encrypt (shifts, message):
    '''Essa função cria a nova mensagem a partir do tipo alternado'''
    novos_caracteres = []
    deslocamento = shifts
    for i in range(len(message)):
        if i > 0:
            deslocamento = - deslocamento
        if deslocamento > 0:
            novo_valor = dicionario[message[i]] + deslocamento
            while novo_valor >= 62:
                novo_valor = novo_valor - 62
            novos_caracteres.append(caracteres_possiveis[novo_valor])
        else:
            novo_valor = dicionario[message[i]] + deslocamento
            while novo_valor < 0:
                novo_valor = novo_valor + 62
            novos_caracteres.append(caracteres_possiveis[novo_valor])  
    mensagem_criptografada = "".join(novos_caracteres)
    return mensagem_criptografada

def variable_shifts_encrypt (shifts, message):
    '''Essa função cria a nova mensagem a partir do tipo variável.'''
    novos_caracteres = []
    for i in range(len(message)):
        if i in range (0,len(message),5):
            deslocamento = int(shifts[0])
        elif i in range (1, len(message),5):
            deslocamento = int(shifts[1])
        elif i in range (2, len(message),5):
            deslocamento = int(shifts[2])
        elif i in range (3, len(message),5):
            deslocamento = int(shifts[3])
        elif i in range (4, len(message),5):
            deslocamento = int(shifts[4])    
        if deslocamento > 0:
            novo_valor = dicionario[message[i]] + deslocamento
            while novo_valor >= 62:
                novo_valor = novo_valor - 62
            novos_caracteres.append(caracteres_possiveis[novo_valor])
        else:
            novo_valor = dicionario[message[i]] + deslocamento
            while novo_valor < 0:
                novo_valor = novo_valor + 62
            novos_caracteres.append(caracteres_possiveis[novo_valor])  
    mensagem_criptografada = "".join(novos_caracteres)
    return mensagem_criptografada

def shift_decrypt (shifts, message):
    '''Essa função é o inverso da shift_encrypt, mudando, apenas, o sinal do valor do shifts.'''
    return shift_encrypt (shifts, message)

def shift_alternate_decrypt (shifts, message):
    '''Essa função é o inverso da shift_alternate_encrypt, mudando, apenas, o sinal do valor do shifts.'''
    return shift_alternate_encrypt (shifts, message)

def variable_shifts_decrypt (shifts, message):
    '''Essa função é o inverso da variable_shifts_encrypt, mudando, apenas, o sinal do valor do shifts.'''
    lista_shifts = []
    for i in range (len(shifts)):
        deslocamento = - shifts[i]
        lista_shifts.append(deslocamento)
    return variable_shifts_encrypt(lista_shifts, message)

while True:
    entrada = input()
    if entrada == "public_key":
        valor_chave_publica = input()
        if is_valid_key(valor_chave_publica) == True:
            print ("Chave pública válida")
        else:
            print ("Chave pública inválida")
    elif entrada == "private_key":
        valor_chave_privada = input()
        if is_valid_key(valor_chave_privada) == True:
            print ("Chave privada válida")
        else:
            print ("Chave privada inválida")
    elif entrada == "encrypt":
        mensagem = input()
        if is_inverse(valor_chave_publica, valor_chave_privada) == True:
            print("Mensagem criptografada:", inverse(mensagem))
        elif find_shifts (valor_chave_publica, valor_chave_privada) != None:
            shifts = find_shifts (valor_chave_publica, valor_chave_privada)
            print("Mensagem criptografada:", shift_encrypt(shifts, mensagem))
        elif find_shifts_alternate (valor_chave_publica, valor_chave_privada) != None:
            shifts = find_shifts_alternate (valor_chave_publica, valor_chave_privada)
            print("Mensagem criptografada:", shift_alternate_encrypt(shifts, mensagem)) 
        else:
            shifts = find_variable_shifts (valor_chave_publica, valor_chave_privada)
            print("Mensagem criptografada:", variable_shifts_encrypt(shifts, mensagem))  
    elif entrada == "decrypt":
        mensagem = input()
        if is_inverse(valor_chave_publica, valor_chave_privada) == True:
            #Como a descriptografia é o processo inverso da criptografia, nesse caso é só não inverter a mensagem.
            print("Mensagem descriptografada:", inverse(mensagem))
        elif find_shifts (valor_chave_publica, valor_chave_privada) != None:
            shifts = find_shifts (valor_chave_publica, valor_chave_privada)
            #Como a descriptografia é o processo inverso da criptografia, nesse caso é só mudar o sinal do shifts.
            print("Mensagem descriptografada:", shift_decrypt(-shifts, mensagem))
        elif find_shifts_alternate (valor_chave_publica, valor_chave_privada) != None:
            shifts = find_shifts_alternate (valor_chave_publica, valor_chave_privada)
            #Como a descriptografia é o processo inverso da criptografia, nesse caso é só mudar o sinal do shifts.            
            print("Mensagem descriptografada:", shift_alternate_decrypt(-shifts, mensagem)) 
        else:
            shifts = find_variable_shifts (valor_chave_publica, valor_chave_privada)
            #Como a descriptografia é o processo inverso da criptografia, nesse caso é só mudar o sinal do shifts.
            print("Mensagem descriptografada:", variable_shifts_decrypt(shifts, mensagem))
        
    elif entrada == "exit":
        break