
def floyd(self,graph):
    nVertices = self.graph.vcount()
    dist = [nVertices][nVertices]
    rotas = [nVertices][nVertices]
    for i in range(nVertices):
        for j in range(nVertices):
            if i == j:
                dist[i][j] = 0
                rotas[i][j] = i
            else:
                dist[i][j] = -1
                rotas[i][j] = -1

    for k in range(nVertices):
        for i in range(nVertices):
            for j in range(nVertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    rotas[i][j] = rotas[i][k]
