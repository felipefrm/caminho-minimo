import math
from igraph import*
class Igraph(Graph):
    def __init__(self,rede):
		super(Igraph, self).__init__()
		#self.nomeRede = rede
    def floyd(self):
        plot(self)
        nVertices = self.vcount()
        dist = [[float('inf') for x in range(nVertices)] for y in range(nVertices)]
        rotas = [[0 for x in range(nVertices)] for y in range(nVertices)]

        for i in range(nVertices):
            for j in range(nVertices):
                if i == j:
                    dist[i][j] = 0
                    rotas[i][j] = i+1
                elif self[i,j] != 0:
                    dist[i][j] = self[i,j]
                    rotas[i][j] = i+1
    
        print(dist)
        print(rotas)
        for k in range(nVertices):
            for i in range(nVertices):
                for j in range(nVertices):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        rotas[i][j] = rotas[i][k]
        print(dist)
        print(rotas)
