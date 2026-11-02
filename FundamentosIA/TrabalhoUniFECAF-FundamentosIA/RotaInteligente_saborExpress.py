# ====== Código SABOR EXPRESS - Rota Inteligente - UniFECAF ======

"""
NOME: HENRIQUE RIBEIRO SIQUEIRA                         DATA: 02/11/2026
MATÉRIA: FUNDAMENTOS DE INTELIGÊNCIA ARTIFICIAL         SEMESTRE: 6º
CURSO: CIÊNCIA DA COMPUTAÇÃO                            R.A.: 50129
"""

import heapq
import math
import random
import statistics

K, CAP, LOJA = 3, 6, 24
SERVICO, PRAZO, VMAX = 2, 60, 40
XY = {7*y+x: (.5*x, .5*y) for y in range(7) for x in range(7)}


def cidade():
    rng, grafo = random.Random(2026), {n: [] for n in XY}
    for y in range(7):
        for x in range(7):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x+dx, y+dy
                if not (0 <= nx < 7 and 0 <= ny < 7):
                    continue
                if dy == 0:
                    if {x, nx} == {3, 4} and y not in (1, 5):
                        continue  # Rio: somente duas pontes.
                    if (y == 2 and dx == -1) or (y == 4 and dx == 1):
                        continue  # Via única.
                if x == nx == 3 and {y, ny} == {2, 3}:
                    continue  # Rua interditada nos dois sentidos.
                pico = 1.65 if 1 <= x <= 5 and 1 <= y <= 5 else 1.1
                minutos = 60*.5/VMAX * pico * rng.uniform(1, 1.45)
                grafo[7*y+x].append((7*ny+nx, minutos, .5))
    return grafo


def astar(grafo, origem, destino):
    h = lambda n: 60*math.dist(XY[n], XY[destino])/VMAX
    fila, custos, pais = [(h(origem), 0, origem)], {origem: 0}, {}
    while fila:
        _, custo, atual = heapq.heappop(fila)
        if custo > custos.get(atual, math.inf)+1e-12:
            continue
        if atual == destino:
            km, n, caminho = 0, destino, [destino]
            while n != origem:
                n, trecho_km = pais[n]
                km += trecho_km
                caminho.append(n)
            return custo, km, caminho[::-1]
        for vizinho, minutos, km in grafo[atual]:
            novo = custo+minutos
            if novo < custos.get(vizinho, math.inf)-1e-12:
                custos[vizinho], pais[vizinho] = novo, (atual, km)
                heapq.heappush(fila, (novo+h(vizinho), novo, vizinho))
    raise ValueError("Destino inalcançável")


def agrupar(pedidos, semente=42):

    # Cada grupo contém índices dos pedidos.
    rng, indices = random.Random(semente), list(range(len(pedidos)))
    ponto = lambda i: XY[pedidos[i]]

    def centro(grupo):
        return tuple(
            sum(ponto(i)[a] for i in grupo)/len(grupo)
            for a in (0, 1)
        )

    def sse(grupo):
        return (
            sum(math.dist(ponto(i), centro(grupo))**2 for i in grupo)
            if grupo else 0
        )

    melhor, menor = None, math.inf
    
    
    for _ in range(10):
        centros = [ponto(rng.choice(indices))]
        while len(centros) < K:
            pesos = [
                min(math.dist(ponto(i), c)**2 for c in centros)
                for i in indices
            ]
            if sum(pesos) <= 1e-15:
                livres = [ponto(i) for i in indices if ponto(i) not in centros]
                centros.append(livres[0] if livres else centros[0])
                continue
            sorteio, escolhido = rng.random()*sum(pesos), len(indices)-1
            for i, peso in enumerate(pesos):
                sorteio -= peso
                if sorteio < 0:
                    escolhido = i
                    break
            centros.append(ponto(escolhido))

        anteriores = None
        for _ in range(100):
            rotulos = [
                min(range(K), key=lambda j:
                    (math.dist(ponto(i), centros[j])**2, j))
                for i in indices
            ]
            grupos = [[i for i in indices if rotulos[i] == j] for j in range(K)]
            for grupo in grupos:
                if not grupo:
                    candidatos = [
                        (math.dist(ponto(i), centros[j])**2, i, j)
                        for j, membros in enumerate(grupos) if len(membros) > 1
                        for i in membros
                    ]
                    _, movido, doador = max(
                        candidatos, key=lambda t: (t[0], t[1])
                    )
                    grupos[doador].remove(movido)
                    grupo.append(movido)
            centros = [centro(g) for g in grupos]
            atuais = tuple(
                next(j for j, g in enumerate(grupos) if i in g)
                for i in indices
            )
            if atuais == anteriores:
                break
            anteriores = atuais

        valor = sum(sse(g) for g in grupos)
        if valor < menor-1e-12:
            melhor, menor = [g[:] for g in grupos], valor


    # Reparo explícito da capacidade pelo menor aumento de SSE.
    while max(map(len, melhor)) > CAP:
        candidatos = []
        for a, grupo in enumerate(melhor):
            if len(grupo) <= CAP:
                continue
            for b, outro in enumerate(melhor):
                if len(outro) >= CAP:
                    continue
                base = sse(grupo)+sse(outro)
                for i in grupo:
                    delta = sse([j for j in grupo if j != i])+sse(outro+[i])-base
                    candidatos.append((delta, i, a, b))
        _, i, a, b = min(candidatos)
        melhor[a].remove(i)
        melhor[b].append(i)
    return melhor


def otimizar(grupo, pedidos, matriz):
    def custo(rota):
        nos = [LOJA]+[pedidos[i] for i in rota]+[LOJA]
        return sum(matriz[a, b][0] for a, b in zip(nos, nos[1:]))

    livres, rota, atual = grupo[:], [], LOJA
    while livres:
        i = min(livres, key=lambda i: (matriz[atual, pedidos[i]][0], i))
        rota.append(i)
        livres.remove(i)
        atual = pedidos[i]

    valor = custo(rota)
    while True:
        melhor, minimo = rota, valor
        for a in range(len(rota)-1):
            for b in range(a+1, len(rota)):
                candidata = rota[:a]+list(reversed(rota[a:b+1]))+rota[b+1:]
                novo = custo(candidata)  # Custo completo do grafo dirigido.
                if novo < minimo-1e-9:
                    melhor, minimo = candidata, novo
        if minimo >= valor-1e-9:
            return rota
        rota, valor = melhor, minimo


def avaliar(grupos, pedidos, matriz):
    assert sorted(i for g in grupos for i in g) == list(range(len(pedidos)))
    assert all(len(g) <= CAP for g in grupos)
    viagem, distancia, duracoes, chegadas = 0, 0, [], []

    for grupo in grupos:
        atual, relogio = LOJA, 0
        for i in grupo:
            minutos, km, _ = matriz[atual, pedidos[i]]
            viagem, distancia = viagem+minutos, distancia+km
            relogio += minutos
            chegadas.append(relogio)
            relogio += SERVICO
            atual = pedidos[i]
        minutos, km, _ = matriz[atual, LOJA]
        viagem, distancia = viagem+minutos, distancia+km
        duracoes.append(relogio+minutos)

    return (
        viagem, distancia, max(duracoes), statistics.mean(chegadas),
        100*sum(t <= PRAZO+1e-9 for t in chegadas)/len(chegadas)
    )


if __name__ == "__main__":
    grafo = cidade()
    pedidos = random.Random(42).sample([n for n in XY if n != LOJA], 18)
    terminais = [LOJA]+pedidos
    matriz = {(a, b): astar(grafo, a, b) for a in terminais for b in terminais}
    manual = [list(range(i, len(pedidos), K)) for i in range(K)]
    variantes = {
        "Manual": manual,
        "NN + 2-opt": [otimizar(g, pedidos, matriz) for g in manual],
        "K-Means + NN + 2-opt": [
            otimizar(g, pedidos, matriz) for g in agrupar(pedidos)
        ]
    }
    print("Método | viagem(min) | km | último retorno | entrega média | pontualidade")
    for nome, grupos in variantes.items():
        print(nome, "|", " | ".join(
            f"{v:.2f}" for v in avaliar(grupos, pedidos, matriz)
        ))
        for entregador, grupo in enumerate(grupos, 1):
            sequencia = " -> ".join(f"P{i+1:02}" for i in grupo)
            print(f"  E{entregador}: loja -> {sequencia} -> loja")
