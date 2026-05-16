def inicio():
    materia = []
    aluno = [materia,]
    peso = int(0)
    soma = int(0)
    for i in range(8):
        nota = float(input('Digite a nota: '))
        pesos = int(input('Digite o peso da nota: '))
        aluno[0].append(nota)
        aluno[0].append(pesos)
        peso = peso + pesos
        soma = (soma + (nota*pesos))
        
    media  = soma / peso
    print(aluno)
    print()
    print(f'A media é : {media:0.2f}')




def entrada(x):
    if x == 's':
        inicio()
    elif x =='n':
        entrada(x = input('Entrar no programa s/n ? '))
entrada(x = input('Entrar no programa s/n ? '))
'''
10
1
9.5
2
8.5
1
7.5
1
6.5
2
5.5
2
4.5
1
3.5
3
'''