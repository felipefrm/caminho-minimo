from igraph import*
from floyd import*
import sys

def imprimeEstatisticas(dist, nVertices):

    arq = open('saida.txt', 'w')

    # arq.write('MATRIZ DE DISTANCIA:\n\n')
    # for i in range(nVertices):
    #     arq.write(str(dist[i]) + '\n')
    # arq.write("\n")

    media = []
    for i in range(nVertices):
        media.append((sum(dist[i])/float(nVertices)))
        arq.write("< Individuo {} >\n".format(i))
        arq.write("Maior caminho: {} ({}x)\n".format(max(dist[i]), dist[i].count(max(dist[i]))))
        arq.write("Menor caminho: {} ({}x)\n".format(min(i for i in dist[i] if i > 0), dist[i].count(min(i for i in dist[i] if i > 0))))
        arq.write("Media: {}\n\n".format(media[i]))

    arq.write("-" * 40)
    arq.write("\nMaior media: {} (individuo {})\n".format(max(media), media.index(max(media))))
    arq.write("Menor media: {} (individuo {})\n".format(min(media), media.index(min(media))))
    arq.write("Media geral: {}\n".format(sum(media)/float(nVertices), media.index(max(media))))
    arq.write("-" * 40)

    d1 = d2 = d3 = 0
    for i in range(nVertices):
        for j in range(i, nVertices):
            if dist[i][j] == 1:
                d1 += 1
            elif dist[i][j] == 2:
                d2 += 1
            elif dist[i][j] >= 3:
                d3 += 1


    arq.write("\nCaminho minimo = 1: {:.2f} %\n".format((d1/float(d1+d2+d3))*100))
    arq.write("Caminho minimo = 2: {:.2f} %\n".format((d2/float(d1+d2+d3))*100))
    arq.write("Caminho minimo = 2: {:.2f} %\n".format((d3/float(d1+d2+d3))*100))

    arq.close()


rede = sys.argv[1]
g = Igraph(rede)
g = g.Read_Ncol(rede, directed = False)
imprimeEstatisticas(g.floyd(), g.vcount())
