def aaa(participantes, candidatos):
    while len(list) < participantes-1:
        chave, nota = input().split(' ')
        chave = str(chave)
        nota = float(nota)
        

        if len(list) == 0:
            list.append(nota)
            
        else:
            cont = int(0)
            for f in range(len(list)):
                
                if nota > list[cont]:
                    list.insert(cont,nota)
                    return 
                elif nota < list[cont]:
                    cont += 1
                    if cont == len(list):
                        list.append(nota)
                        return 
                    
                    
                    
                    
        
    print(list)
participantes, candidatos = input().split(' ')
participantes = int(participantes)
candidatos = int(candidatos)
print(participantes, candidatos)
list = []
aaa(participantes, candidatos)

'''
1 9.2
2 8.5
3 9.9
4 6.7
5 7.3
'''