def fun2(TAMANHO, PALAV, FALSO):
    print('ok2')
def fun1(TAMANHO, PALAV, VERDADEIRO):
    print('ok1')
    


def entrar(entrada):
    if entrada == '1':
        TAMANHO = int(0)
        PALAV = int(0)
        VERDADEIRO = int(0)
        return fun1(TAMANHO, PALAV, VERDADEIRO)
    elif entrada == 'A':
        TAMANHO = int(0)
        PALAV = int(0)
        FALSO = int(0)
        return fun2(TAMANHO, PALAV, FALSO)
entrar(entrada = input(f'Digite uma palavra , a quantidade de caracteres da esquerda para a direita A extrair, e o número 1 se quiser ver em maiúsculo: '))
