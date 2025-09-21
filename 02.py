entrada = int(input('Entre com um número entre(0/999), finalize com 999: '))
total  = int(0)
quantidade = int(0)
    
def inicio(entrada, quantidade, total):
    
    if entrada >= 999:
        print(f'Números maiores que 10 foram: {quantidade}, e as somas totalizaram: {total}')
        print('Fim da execução do programa !')

    elif entrada < 10:
        ### NOVA ENTRADA ###
        print('')
        print('Insira uma númeração maior que 9 !')
        print('')
        entrada = int(input('Entre com um número: '))


        return inicio(entrada, quantidade, total)
        
    elif entrada >= 10:
        print('')
        print(f'Foi Alocado a Entrada {quantidade+1}: ', entrada)
        print('')
        
        quantidade  = quantidade + 1
        total  = total + entrada
        
        ### NOVA ENTRADA ###
        entrada = int(input('Entre com um número: '))

        return inicio(entrada, quantidade, total)
    
inicio(entrada, quantidade, total)
        
