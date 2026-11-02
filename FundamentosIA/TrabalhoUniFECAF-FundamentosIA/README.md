# Projeto Rota Inteligente — Restaurante Sabor Express

Tema: Otimização de entregas utilizando Inteligência Artificial, algoritmos de busca em grafos e agrupamento de dados.

## 1. Descrição do problema, desafio proposto e objetivos

O restaurante Sabor Express enfrenta desafios relacionados à organização e à eficiência das entregas de pedidos. Com o aumento da demanda, torna-se necessário planejar rotas que permitam aos entregadores atender vários clientes, reduzindo o tempo de deslocamento, o consumo de combustível e os custos operacionais.

O principal problema está na definição das melhores rotas de entrega. Quando o planejamento é realizado manualmente ou sem critérios de otimização, os entregadores podem percorrer distâncias desnecessárias, enfrentar atrasos e realizar trajetos pouco eficientes.

### Desafio proposto

Desenvolver um sistema inteligente em Python capaz de calcular rotas otimizadas, agrupar pedidos próximos geograficamente e organizar múltiplas entregas utilizando algoritmos de Inteligência Artificial.

### Objetivos

- Encontrar os caminhos de menor custo entre o restaurante e os clientes.
- Agrupar pedidos próximos utilizando K-Means.
- Aplicar algoritmos de busca, como A\*, BFS e DFS.
- Reduzir a distância total percorrida pelos entregadores.
- Comparar o desempenho dos algoritmos utilizados.
- Visualizar rotas, pontos de entrega e métricas em uma interface Streamlit.
- Melhorar a eficiência operacional e a qualidade do serviço.

## 2. Explicação detalhada da abordagem adotada

A solução proposta utiliza uma abordagem híbrida, combinando algoritmos de busca em grafos, técnicas de agrupamento e otimização de rotas.

### Fluxo de funcionamento do sistema

1\. Cadastro dos pedidos

Localização dos clientes e informações das entregas

2\. Construção do grafo

Ruas, cruzamentos, distâncias e conexões

3\. Agrupamento K-Means

Divisão dos pedidos por proximidade geográfica

4\. Busca e otimização de rotas

A\*, BFS, DFS e definição da sequência de entregas

5\. Visualização e avaliação

Streamlit, rotas calculadas e indicadores de desempenho

O processo começa com o cadastro dos pedidos e suas respectivas localizações. Essas informações são representadas em um grafo, no qual os vértices representam o restaurante, os clientes e os cruzamentos, enquanto as arestas representam as conexões entre esses pontos.

Em seguida, o algoritmo K-Means agrupa os clientes conforme sua proximidade geográfica. Isso permite distribuir os pedidos entre diferentes entregadores.

Após o agrupamento, o algoritmo A\* identifica os caminhos de menor custo entre os pontos. Uma etapa adicional determina a melhor ordem para visitar os clientes, evitando deslocamentos desnecessários.

Por fim, o sistema apresenta os resultados em uma interface desenvolvida com Streamlit, permitindo visualizar as rotas e analisar indicadores de desempenho.

## 3. Algoritmos utilizados

| Algoritmo                        | Aplicação no Sabor Express                                                 |
| -------------------------------- | -------------------------------------------------------------------------- |
| A (A-estrela)\*                  | Encontrar caminhos de menor custo usando uma heurística de distância.      |
| BFS (Busca em Largura)           | Encontrar caminhos com o menor número de arestas em grafos não ponderados. |
| DFS (Busca em Profundidade)      | Explorar caminhos e verificar a conectividade do grafo.                    |
| K-Means                          | Agrupar clientes próximos e auxiliar na distribuição de entregas.          |
| Otimização de múltiplas entregas | Definir a sequência de visitas para minimizar o custo total da rota.       |

### Algoritmo A\*

O A\* utiliza a função:

\\[ f(n)=g(n)+h(n) \\]

Em que:

- \\(g(n)\\): custo acumulado desde o ponto inicial.
- \\(h(n)\\): estimativa do custo restante até o destino.
- \\(f(n)\\): custo total estimado.

O A\* pode garantir o caminho ótimo quando a heurística é admissível e as demais condições do algoritmo são atendidas.

### Algoritmo K-Means

O K-Means organiza os clientes em grupos, minimizando a soma das distâncias quadráticas entre cada ponto e o centro de seu grupo.

\\[ J=\sum\_{i=1}^{k}\sum\_{x\in C_i}\\|x-\mu_i\\|^2 \\]

Em que \\(k\\) representa a quantidade de grupos, \\(C_i\\) representa os clientes do grupo e \\(\mu_i\\) seu centroide.

O agrupamento geográfico é uma etapa inicial: a atribuição definitiva das entregas também deve considerar capacidade dos entregadores e distâncias reais pelas ruas.

## 4. Diagrama do grafo utilizado na solução

O diagrama abaixo representa um cenário ilustrativo do restaurante Sabor Express com seis clientes e diferentes conexões de entrega.

Restaurante

Conexões

Clientes

Nesse modelo, o restaurante é representado pelo vértice R. Os pontos A e B funcionam como conexões intermediárias, enquanto C, D, E e F representam destinos de entrega.

As arestas possuem pesos associados ao custo de deslocamento. Esses pesos podem representar distâncias, tempos ou outros custos, desde que sejam utilizados de maneira consistente.

Por exemplo, para alcançar o cliente E, o A\* pode selecionar o caminho R → B → E, cujo custo ilustrativo é \\(4+2=6\\).

## 5. Análise dos resultados e eficiência da solução

Como não foram fornecidas medições de uma execução real do projeto, a tabela abaixo apresenta uma simulação ilustrativa, utilizada para demonstrar como os resultados podem ser avaliados.

| Indicador            | Sem otimização | Com otimização | Melhoria |
| -------------------- | -------------- | -------------- | -------- |
| Distância total      | 40 km          | 29 km          | 27,5%    |
| Tempo total          | 120 min        | 90 min         | 25%      |
| Consumo estimado     | 2,0 L          | 1,45 L         | 27,5%    |
| Custo de combustível | R$ 12,00       | R$ 8,70        | 27,5%    |

Comparação ilustrativa da distância percorrida

Distância total em quilômetros

0 km15 km30 km45 kmSem otimizaçãoCom otimização

Os valores simulados indicam que a combinação dos algoritmos pode reduzir os deslocamentos e os custos operacionais. Entretanto, a economia efetiva precisa ser validada com pedidos reais, distâncias rodoviárias e condições de trânsito.

### Eficiência dos algoritmos

O A\* tende a ser mais eficiente que buscas sem heurística em problemas de caminhos mínimos quando utiliza uma estimativa informativa. O BFS é útil em grafos não ponderados, enquanto o DFS permite explorar a conectividade, mas não garante o caminho de menor custo.

O K-Means facilita a organização das entregas, embora não garanta que os grupos produzam as melhores rotas viárias.

## 6. Limitações encontradas

Entre as principais limitações da solução proposta estão:

- Trânsito em tempo real: o modelo pode não considerar congestionamentos, acidentes e interdições.
- Distância geográfica: a proximidade em linha reta não representa necessariamente a menor distância pelas ruas.
- Capacidade dos entregadores: o agrupamento precisa considerar quantos pedidos cada entregador consegue transportar.
- Escalabilidade: o aumento do número de clientes torna a otimização combinatória mais complexa.
- Dados simulados: resultados obtidos com cenários artificiais podem não refletir o desempenho real do restaurante.

## 7. Sugestões de melhoria

Para aprimorar o sistema Sabor Express, recomenda-se integrar APIs de mapas, como Google Maps ou OpenStreetMap, para trabalhar com redes viárias reais.

Também seria interessante utilizar bibliotecas de otimização, como Google OR-Tools, para resolver o Problema de Roteamento de Veículos (VRP), considerando múltiplos entregadores, capacidade e restrições de tempo.

Outra melhoria seria incorporar modelos de Machine Learning para prever a duração das entregas com base no horário, região, distância e histórico de pedidos.

Por fim, a interface Streamlit poderia apresentar mapas interativos, relatórios de desempenho e comparações entre rotas planejadas e efetivamente realizadas.

## 8. Conclusão

O projeto Rota Inteligente — Sabor Express demonstra como técnicas de Inteligência Artificial podem ser aplicadas à otimização logística de um restaurante.

A combinação dos algoritmos A\*, BFS, DFS e K-Means permite estruturar uma solução capaz de representar a rede de entregas, explorar caminhos, agrupar clientes e apoiar a escolha de rotas mais eficientes.

A principal contribuição do projeto está na possibilidade de transformar o planejamento manual em um processo automatizado, orientado por dados e indicadores de desempenho.

Embora existam limitações relacionadas ao trânsito, à capacidade operacional e à qualidade dos dados, a solução apresenta potencial para reduzir custos, melhorar a produtividade dos entregadores e aumentar a satisfação dos clientes.

Assim, o Sabor Express constitui uma aplicação prática dos conceitos de grafos, algoritmos de busca, agrupamento e otimização estudados em Inteligência Artificial.
