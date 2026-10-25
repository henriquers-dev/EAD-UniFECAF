# Sabor Express — Rota Inteligente

Requer Python 3.10 ou superior. Não precisa instalar bibliotecas.

Na raiz do repositório:

```bash
python3 FundamentosIA/rota_inteligente.py --pedidos 20 --entregadores 3 --seed 42
python3 -m unittest discover -s FundamentosIA -p 'test_rota*.py' -v
```

O resultado JSON compara distribuição circular na ordem de chegada, K-Means com ordem de chegada e K-Means com vizinho mais próximo e 2-opt. Todas as alternativas usam os mesmos caminhos mínimos A*, ruas e tempos. As rotas começam e terminam no restaurante `(0, 0)`. Coordenadas dos nós são índices da malha; cada quarteirão mede 0,5 km.

A cidade possui 64 pontos, sentidos únicos e velocidades simuladas entre 12 e 40 km/h. O anel externo é bidirecional. A heurística A* usa distância euclidiana dividida por 40 km/h, um limite inferior do tempo de viagem. A distância reportada corresponde ao percurso escolhido por tempo, não necessariamente ao menor percurso por distância.

K-Means é implementado em Python, sem dependências, e considera coordenadas cartesianas. Ele não impõe capacidade nem equilibra o número de pedidos. A otimização 2-opt recalcula todo o custo dirigido, pois inverter uma sequência pode mudar os caminhos de ida e volta. O resultado nunca piora a ordem de chegada dentro do mesmo agrupamento; a combinação com agrupamento não garante superar a referência global em todo cenário.

Exemplo com seed 42, 20 pedidos e 3 entregadores: tempo total de percurso de 157,029 para 84,258 minutos; distância de 66 para 34 km. A soma dos tempos dos entregadores não é o tempo de conclusão da frota: essa métrica é apresentada separadamente como maior tempo individual. Os resultados não incluem preparo, atendimento, espera ou trânsito em tempo real. Não há garantia de ótimo global, suporte a múltiplos pedidos no mesmo destino ou janelas de entrega.

A matriz de caminhos calcula A* para todos os pares de destinos e mantém seus percursos em memória. Essa abordagem atende à simulação pequena (até 63 pedidos); grandes volumes exigiriam outra estratégia de armazenamento e cálculo.

