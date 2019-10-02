from igraph import*

class Igraph(Graph):

    def __init__(self,rede):
		super(Igraph, self).__init__()

    def floyd(self):
        nVertices = self.vcount()
        plot(self, vertex_label=[i for i in range(nVertices)])
        dist = [[float('inf') for x in range(nVertices)] for y in range(nVertices)]
        rotas = [[0 for x in range(nVertices)] for y in range(nVertices) ]

        for i in range(nVertices):
            for j in range(nVertices):
                if i == j:
                    dist[i][j] = 0
                    rotas[i][j] = i+1
                elif self[i,j] != 0:
                    dist[i][j] = 1
                    rotas[i][j] = i+1

        for k in range(nVertices):
            for i in range(nVertices):
                for j in range(nVertices):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        rotas[i][j] = rotas[i][k]

        return dist
