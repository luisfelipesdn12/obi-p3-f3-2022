n_salas, k_radares = map(int, input().split())
caminhos = {
    s: [] for s in range(1, n_salas + 1)
}

for _ in range(n_salas - 1):
    a, b = map(int, input().split())
    caminhos[a].append(b)

resultado = None
raio = 1

while resultado is None:
    for sala in range(1, n_salas + 1):
        segura = {
            s: False for s in range(1, n_salas + 1)
        }
        segura[sala] = True
        
        if raio == 1:
            for adj in caminhos[sala]:
                segura[adj] = True
        else:
            pass
        
        if False not in segura.values():
            resultado = raio
            break
    
    raio += 1
    
print(resultado)
