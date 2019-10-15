from igraph import*
from floyd import*
import sys

def calculaPorcentagem(dist, nVertices):
    d = [0, 0, 0]
    for i in range(nVertices):
        for j in range(i+1, nVertices):
            if dist[i][j] == 1:
                d[0] += 1
            elif dist[i][j] == 2:
                d[1] += 1
            elif dist[i][j] >= 3:
                d[2] += 1
    return d

def imprimeEstatisticas(dist, nVertices):

    individual = open('resultados_individuais.txt', 'w')

    # individual.write('MATRIZ DE DISTANCIA:\n\n')
    # for i in range(nVertices):
    #     individual.write(str(dist[i]) + '\n')
    # individual.write("\n")

    media = []
    for i in range(nVertices):
        media.append((sum(dist[i])/float(nVertices)))       # imprime maior e menor caminho de cada individuo
        individual.write("< Individuo {} >\n".format(i))
        individual.write("Maior caminho: {} ({}x)\n".format(max(dist[i]), dist[i].count(max(dist[i]))))
        individual.write("Menor caminho: {} ({}x)\n".format(min(i for i in dist[i] if i > 0), dist[i].count(min(i for i in dist[i] if i > 0))))
        individual.write("Media: {}\n\n".format(media[i]))

    individual.close()

    geral = open('resultado_geral.txt', 'w')                # imprime dados gerais obtidos na execucao

    geral.write("-" * 40)
    geral.write("\nMaior media: {} (individuo {})\n".format(max(media), media.index(max(media))))
    geral.write("Menor media: {} (individuo {})\n".format(min(media), media.index(min(media))))
    geral.write("Media geral: {}\n".format(sum(media)/float(nVertices), media.index(max(media))))
    geral.write("-" * 40)

    d = calculaPorcentagem(dist, nVertices)
    geral.write("\nCaminho minimo = 1: {:.2f} %\n".format((d[0]/float(sum(d)))*100))
    geral.write("Caminho minimo = 2: {:.2f} %\n".format((d[1]/float(sum(d)))*100))
    geral.write("Caminho minimo = 3: {:.2f} %\n".format((d[2]/float(sum(d)))*100))
    geral.write("-" * 40)

    geral.close()



rede = sys.argv[1]      # le o arquivo passado por argumento no terminal
g = Igraph(rede)        # cria o grafo
g = g.Read_Ncol(rede, directed = False)     # le o arquivo contendo o grafo
imprimeEstatisticas(g.floyd(), g.vcount())  # executa o floyd e imprime os dados
