from math import inf

n, k = map(int, input().split())
alturas = list(map(int, input().split()))
moedas = 0

ocorrencias = {
    a: alturas.count(a) for a in alturas
}

# o maior tem que estar nos k mais recorrentes
# pois n pode ser subtraido
ocorrencias[max(alturas)] = inf

# k mais recorentes
mais_ocorr = sorted(
    ocorrencias.keys(),
    key=lambda x: ocorrencias[x],
    reverse=True
)[0:k]

for a in alturas:
    if a not in mais_ocorr:
        for o in ocorrencias:
            if o > a:
                moedas += o - a
                break

print(moedas)
