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

    # tamanho adicional (aumento de digitos)
    ta = 0

    while p+t <= n:

        # dígito obtido
        d = int("".join(digitos[p:p+t+ta]))
        # print(f"d: {d} (ta: {ta})")

        if da == None: pass
        elif da + 1 == d: pass
        else:
            wrong = True
            break

        da = d
        p += t + ta

        if len(str(d + 1)) > len(str(d)): ta += 1

    # print(f"wrong: {wrong}")
    
    if wrong == False: break

    t += 1

a = int("".join(digitos[0:t]))
print(a)
