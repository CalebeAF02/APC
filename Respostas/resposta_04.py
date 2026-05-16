entrada = int(input())
contagem_pares = int(0)
soma = int(0)

def inicio(entrada,contagem_pares,soma):
    contagem_pares = contagem_pares + 2
    
    while contagem_pares <= entrada :
        soma = soma + contagem_pares
        contagem_pares = contagem_pares + 2
    print(f'O somatório é: {soma}')
    
inicio(entrada,contagem_pares,soma)

''' inicio

execução 10

0+2 = 2

2+4 = 6

6+6 = 12

12+8 = 20

20+10 = 30

Fim '''