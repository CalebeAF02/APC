def CARACTERE(TAMANHO, PALAVRA, LOGICO):
    if LOGICO == True :
        for i in range(len(PALAVRA)):
            if i < TAMANHO:
                print(palavra[i])
            else:
                pass
        
    elif LOGICO == False :
        for i in range(len(PALAVRA)):
            if i < TAMANHO:
                print(palavra[i])
            else:
                pass
        
    

def entrar(entrada):
    print(PALAVRA, TAMANHO, LOGICO)
    
    TAMANHO = int(TAMANHO)
    PALAVRA = str(PALAVRA)

    if LOGICO == '1':
        CARACTERE(TAMANHO, PALAVRA, VERDADEIRO)
    elif LOGICO == '2':
        CARACTERE(TAMANHO, PALAVRA, FALSO)
        
entrar(PALAVRA, TAMANHO, LOGICO = input('Digite uma palavra, a quantidade de caracteres da esquerda para a direita A extrair, e o número 1 quiser ver em maiusculo, ou 2 se minúsculo: ex:(palavra, 7, 2)').split())
