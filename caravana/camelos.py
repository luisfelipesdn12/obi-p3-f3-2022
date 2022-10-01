n = int(input())
pesos = [int(input()) for _ in range(n)]
media = int(sum(pesos) / n)

for p in pesos:
    print(media - p)
