class No:
    def __init__(self, valor):
        self.valor = valor
        self.numero_esquerdo = None
        self.numero_direito = None

# Construindo a árvore

raiz = No(8)
raiz.numero_esquerdo = No(3)
raiz.numero_direito = No(10)
raiz.numero_esquerdo.numero_esquerdo = No(1)
raiz.numero_esquerdo.numero_direito = No(6)
raiz.numero_esquerdo.numero_direito.numero_esquerdo = No(4)
raiz.numero_esquerdo.numero_direito.numero_direito = No(7)
raiz.numero_direito.numero_direito = No(14)
raiz.numero_direito.numero_direito.numero_esquerdo = No(13)

print(raiz.numero_esquerdo)
