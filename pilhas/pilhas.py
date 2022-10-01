n, k = map(int, input().split())
alturas = list(map(int, input().split()))
moedas = 0

# 13 pontos com k = 1
alt_max = max(alturas)
for i in range(len(alturas)):
    # print(i)
    moedas += alt_max - alturas[i]

print(moedas)
