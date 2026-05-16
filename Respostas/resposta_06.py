
##################################################
def inicio():
    texto = []
    position = []
    
    conteudo = str(input('Digite um texto: '))
    caracter = str(input('Agora digite um algoritimo ou uma letra a ser pesquisada: '))
    
    cont= int(1)
    for item in conteudo :
        texto.append(item)
        if item == caracter:
            position.append(cont)
            cont+=1
        else:
            cont+=1
    if 0 == len(position):
        print('Caractere não encontrado no texto! ')
    elif 1 == len(position):
        print(f'Encontrado na posição {position[0]}')
    else:
        print(position)
        print(f'Encontrados os caracteres no texto nas posições: ')
       
        for i in range(len(position)):
            print(f'- posição {position[i]}')
            
        
    
    '''
    conteudo.split()
    print(conteudo.split())
    '''
    print()
    novamente = input('Tentar Novamente (s/n) ? ')
    if novamente == 's':
        inicio()
    else:
        return
###################################################
programa = input('Abrir programa (s/n) ? ')
while programa != 's':
    programa = input('Abrir programa (s/n) ? ')
    
if programa == 's':
    inicio()
    