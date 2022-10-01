n, k = map(int, input().split())
alturas = list(map(int, input().split()))
moedas = 0

# os K maiores valores
k_max = sorted(set(alturas), reverse=True)[0:k]
# print(f"k_max: {k_max}")

# o menos maior valor
min_max = min(k_max)
# print(f"min_max: {min_max}")

for a in alturas:
    # print(f"a: {a} ({min_max - a})")
    if a < min_max:
        moedas += min_max - a

print(moedas)
