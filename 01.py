print('Entre com 3 números diferentes. Ex: 1 2 3: ')

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

def inicio(a, b, c):
    if a<b:
        if b<c:
            #print(a, b, c)
            print(f'{a} {b} {c}')
        else:
            if c<a:
                #print(c, a, b)
                print(f'{c} {a} {b}')
            else:
                #print(a, c, b)
                print(f'{a} {c} {b}')
    else:
        if a<c:
            #print(b, a, c)
            print(f'{b} {a} {c}')
        else:
            if c<b:
                #print(c, b, a)
                print(f'{c} {b} {a}')
            else:
                #print(b, c, a)
                print(f'{b} {c} {a}')
inicio(a, b, c)
            