def Fim(opc):
    print()
    print('Ola você acessou a opção', opc,'. Tecle <Enter>: ')
    print('Programa finalizado !')
def Listagem(opc):
    print()
    print('Ola você acessou a opção', opc,'. Tecle <Enter>: ')
def Consulta(opc):
    print()
    print('Ola você acessou a opção', opc,'. Tecle <Enter>: ')
def Cadastramento(opc):
    print()
    print('Ola você acessou a opção', opc,'. Tecle <Enter>: ')    


def entrada(opc = input("Escolha uma opc: 1 - Cadastramento | 2 - Consulta | 3 - Listagem | 4 - Fim | ")):
    while opc != '1' or '2' or '3' or '4':
        if opc == '1':
            Cadastramento(opc)
            print()
            return entrada(opc = input("Escolha uma opc: 1 - Cadastramento | 2 - Consulta | 3 - Listagem | 4 - Fim | "))

        elif opc == '2':
            Consulta(opc)
            print()
            return entrada(opc = input("Escolha uma opc: 1 - Cadastramento | 2 - Consulta | 3 - Listagem | 4 - Fim | "))
        elif opc == '3':
            Listagem(opc)
            print()
            return entrada(opc = input("Escolha uma opc: 1 - Cadastramento | 2 - Consulta | 3 - Listagem | 4 - Fim | "))
        elif opc == '4':
            Fim(opc)
            print()
            return entrada(opc = input("Escolha uma opc: 1 - Cadastramento | 2 - Consulta | 3 - Listagem | 4 - Fim | "))


        return entrada(opc = input("Escolha uma opc: 1 - Cadastramento | 2 - Consulta | 3 - Listagem | 4 - Fim | "))

    else:
        Print('ok')
entrada()

    
     
