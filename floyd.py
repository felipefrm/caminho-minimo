from igraph import*

def imprime(dist, nVertices):

    arq = open('saida.txt', 'w')
    arq.write('MATRIZ DE DISTANCIA:\n\n')
    for i in range(nVertices):
        arq.write(str(dist[i]) + '\n')

    for i in range(nVertices):
        arq.write("\nSaindo do vertice {}: ".format(i))
        arq.write("Maior caminho: {} ({}-{}) / Menor caminho: {} ({}-{}) / Media: {}".format(max(dist[i]), i, dist[i].index(max(dist[i])), min(dist[i]), i, dist[i].index(min(dist[i])), sum(dist[i])/nVertices))

    arq.close()

class Igraph(Graph):
    def __init__(self,rede):
		super(Igraph, self).__init__()
		#self.nomeRede = rede
    def floyd(self):
        # plot(self)
        nVertices = self.vcount()
        dist = [[float('inf') for x in range(nVertices)] for y in range(nVertices)]
        rotas = [[0 for x in range(nVertices)] for y in range(nVertices) ]

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
        
        imprime(dist, nVertices)
