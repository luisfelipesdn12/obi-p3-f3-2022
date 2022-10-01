n = int(input())
digitos = input().split()

# tamanho do teste
t = 1

while t <= n:
    # digito anterior
    da = None
    
    # posição inicial do teste
    p = 0
    
    # tamanho está errado
    wrong = False

    while p+t <= n:
        # dígito obtido
        d = int("".join(digitos[p:p+t]))
        # print(d)

        if da == None: pass
        elif da + 1 == d: pass
        else:
            wrong = True
            break

        da = d
        p += t

    # print(wrong)
    
    if wrong == False: break

    t += 1

a = int("".join(digitos[0:t]))
print(a)
