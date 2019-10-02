from floyd import*
from igraph import*
import sys

rede = sys.argv[1]
#url = rede+".txt"
g = Igraph(rede)
g = g.Read_Ncol(rede, directed = False)
g.floyd()
