import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

Label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']

def le_grafo(file):
    grafo = {}
    # Leitura de dados
    with open(file, "r") as f:
        vertices = int(f.readline())
        # Criação do grafo com dict
        for i in f:
            v1, v2, peso = map(int, i.strip().split())
            if v1 not in grafo:
                grafo[v1] = []
            if v2 not in grafo:
                grafo[v2] = []

            adjacencia = [v2, peso]
            # Criando grafo com dicionario
            grafo[v1].append(adjacencia)
        #print(grafo)
        return [vertices, grafo]



def dijkstra(grafo, vertice):
    # Inicialização
    d = []
    pai = []
    caminho = []
    for v in range(len(grafo)):
        d.append(float("+infinity"))
        pai.append(None)
        caminho.append(False)

    d[vertice-1] = 0


    for i in range(len(grafo)):

        # Pega a menor distancia
        Dmin = None
        for v in range(len(d)):  # for each v in g.V
            if not caminho[v]:
                if Dmin == None:
                    Dmin = v
                elif d[v] < d[Dmin]:
                    Dmin = v

        # Algoritimo
        caminho[Dmin] = True
        for v, peso in grafo[Dmin+1]:
            if d[v-1] > d[Dmin] + peso:
                d[v-1] = d[Dmin] + peso
                pai[v-1] = Dmin+1


    print("Distancia = ",d)

    # Com Legenda
    for i in range(len(pai)):
        if pai[i] == None:
            G.add_node(Label[i])
            continue
        G.add_edge(Label[i], Label[pai[i]-1], weigth=d[i])

    # Com numeros
    # for i in range(len(pai)):
    #     if pai[i] == None:
    #         G.add_node(i+1)
    #         continue
    #     G.add_edge(i+1, pai[i], weigth=d[i])


def imprimeGrafo(grafo):
    print("{")
    for i in range(len(grafo)):
        print(" ", i+1, ":", grafo[i+1])
    print("}")
    print()


def main():
    vertices, grafo = le_grafo("grafo2.txt")
    imprimeGrafo(grafo)

    # Algoritimo
    dijkstra(grafo, 5)

    # Plot da arvore
    nx.draw(G, with_labels=True, node_color='yellow', node_size=1000)
    plt.show()


main()
