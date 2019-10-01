from floyd import*
import sys
from igraph import*
rede = sys.argv[1]
#url = rede+".txt"
g = Igraph(rede)
print("ok")
g = g.Read_Ncol(rede)
g.floyd()
