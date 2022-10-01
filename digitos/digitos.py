# primeiro, pegamos a quantidade de dígitos
# que serão inseridos
n = int(input())

# depois, lemos os dígitos e os armazenamos
# em uma lista de caractéres
digitos = input().split()

# tamanho do teste
# define qual é o tamanho que estamos
# testando X (tamanho 1), XX (tamanho 2)
t = 1

# o tamanho pode ser no máximo a quantidade
# de dígitos inseridos
while t <= n:
    # digito anterior
    # vai armazenar o dígito que foi encontrado
    # na repetição anterior (serve pra testar se
    # o próximo dígito é a sequencia deste)
    da = None
    
    # posição inicial do teste
    # uma espécie de ponteiro indicando em qual
    # parte dos dígitos inseridos estamos começando
    # a considerar como o dígito atual
    p = 0

    # tamanho está errado
    # se algum dígito não for a sequência do anterior
    # está variável se tornará True, indicando que o
    # tamanho considerado no teste está errado
    wrong = False

    # tamanho adicional (aumento de digitos)
    # se começamos, por exemplo, com o tamanho 1,
    # temos 1, 2, 3, etc. mas quando chegarmos ao
    # 9, precisamos aumentar o tamanho da sequência
    # pra 2 pra considerar o 10.
    ta = 0

    # o tamanho considerado não pode ser maior do que
    # a quantidade de dígitos inseridos
    while p+t+ta <= n:
        # dígito obtido
        # o dígito atual, extraído da sequência
        # a parit da posição inicial
        d = int("".join(digitos[p:p+t+ta]))
        # print(f"d: {d} (ta: {ta})")

        # se não houver um dígito anterior
        # para ser testado, vai pro próximo
        # (esse tamanho ainda pode estar correto)
        if da == None: pass
        # se o dígito atual for o sucessor do
        # anterior, vai pro próximo
        # (esse tamanho ainda pode estar correto)
        elif da + 1 == d: pass
        # se não for, o tamanho está errado
        # quebra a repetição e vai para o próximo
        # tamanho a ser testado
        else:
            wrong = True
            break

        # define que a partir de agora o dígito
        # anterior é o que foi considerado nessa
        # repetição
        da = d

        # define que a próxima posição a ser
        # contada é a que vem depois do tamanho
        # do dígito considerado
        p += t + ta

        # caso o dígito atual +1, for maior em
        # tamanho de texto que o atual, considera
        # esse aumento de tamanho
        if len(str(d + 1)) > len(str(d)): ta += 1

    # print(f"wrong: {wrong}")

    # após todos os testes com esse tamanho,
    # se ele não estiver errado, pare de testar
    if wrong == False: break

    # se ele estiver errado, aumente em 1
    # e testa novamente
    t += 1

# no final, o primeiro dígito (A) da sequência
# é o formado pelos T primeiros dígitos da
# sequência inserida
a = int("".join(digitos[0:t]))
print(a)
