from floyd import*
from igraph import*
import sys

def imprimeEstatisticas(dist, nVertices):

    arq = open('saida.txt', 'w')
    # arq.write('MATRIZ DE DISTANCIA:\n\n')
    # for i in range(nVertices):
    #     arq.write(str(dist[i]) + '\n')

    media = []
    for i in range(nVertices):
        media.append((sum(dist[i])/float(nVertices)))
        arq.write("\nSaindo do vertice {}\n".format(i))
        arq.write("Maior caminho: {} ({}x)\n".format(max(dist[i]), dist[i].count(max(dist[i]))))
        arq.write("Menor caminho: {} ({}x)\n".format(min(i for i in dist[i] if i > 0), dist[i].count(min(dist[i]))))
        arq.write("Media: {}\n".format(media[i]))
    arq.write("\nMaior media: {} (formiga {})\n".format(max(media), media.index(max(media))))
    arq.close()


rede = sys.argv[1]
#url = rede+".txt"
g = Igraph(rede)
g = g.Read_Ncol(rede, directed = False)
imprimeEstatisticas(g.floyd(), g.vcount())
