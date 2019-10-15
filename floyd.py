#coding: utf-8
from igraph import*

class Igraph(Graph):

    def __init__(self,rede):
		super(Igraph, self).__init__()

    def floyd(self):
        nVertices = self.vcount()   # quantidade de vertices
        # plot(self, vertex_label=[i for i in range(nVertices))
        dist = [[float('inf') for x in range(nVertices)] for y in range(nVertices)]     # preenche a matriz de distancia com 'inf'

        for i in range(nVertices):
            for j in range(nVertices):
                if i == j:              # se estiver na diagonal principal, dist = 0
                    dist[i][j] = 0
                elif self[i,j] != 0:    # se houver aresta entre os vertices, dist = 1
                    dist[i][j] = 1

        for k in range(nVertices):
            for i in range(nVertices):
                for j in range(nVertices):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                            # verifica se é melhor manter a dist[i][j] atual ou atualizar
        return dist
