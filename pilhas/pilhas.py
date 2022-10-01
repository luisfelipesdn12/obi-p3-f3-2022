n, k = map(int, input().split())
alturas = list(map(int, input().split()))
moedas = 0

# os K maiores valores
k_max = sorted(alturas, reverse=True)[0:k]

# o menos maior valor
min_max = min(k_max)

for a in alturas:
    if a < min_max:
        moedas = min_max - a

print(moedas)
