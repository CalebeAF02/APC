entrada = int(input())
quantidade = int(0)
total = int(0)
def inicio(entrada,quantidade,total):
    while entrada>10 and entrada<999 :
        print(entrada)
        quantidade = quantidade+1
        total = total+entrada
        
        entrada = int(input())
        return inicio(entrada,quantidade,total)
    if entrada == 999:
        print('Números maiores que 10 foram :', quantidade, end='')
        print(', e totalizaram: ', total)
        
        print('Finalizar Programa')
        
inicio(entrada,quantidade,total)
