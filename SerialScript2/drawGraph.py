import networkx as nx
import matplotlib.pyplot as plt
import array
import os
protocol = 3
if protocol == 3:
    dir = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPL3-PeriodicBackward\OutputTopology.txt"
    delDir = "C:/Users/zhoul/PycharmProjects/SerialScript2/WAMPL3-PeriodicBackward/Topo"
elif protocol == 1:
    dir = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPLproject\OutputTopology.txt"
    delDir = "C:/Users/zhoul/PycharmProjects/SerialScript2/WAMPLproject/Topo"
delList=os.listdir(delDir)
for f in delList:
 filePath = os.path.join( delDir, f )
 if os.path.isfile(filePath):
  os.remove(filePath)

G = nx.DiGraph()
G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
nodePos = {
    0: array.array('i', [4, 1]),
    1: array.array('i', [6, 1]),
    3: array.array('i', [3, 2]),
    2: array.array('i', [5, 2]),
    4: array.array('i', [7, 2]),
    7: array.array('i', [2, 3]),
    5: array.array('i', [4, 3]),
    6: array.array('i', [6, 3]),
    8: array.array('i', [8, 3]),
    12: array.array('i', [1, 4]),
    9: array.array('i', [3, 4]),
    10: array.array('i', [5, 4]),
    11: array.array('i', [7, 4]),
    13: array.array('i', [9, 4])
}
x=[5,3,7,4,6,2,8,3,5,7,1,9]
y=[2,2,2,3,3,3,3,4,4,4,4,4]

with open(dir) as f:
    lines = f.readlines()
fignum=1
linepre = lines[0]
for line in lines:
    if line != linepre or fignum == 1:
        pre = line.split(',')
        num= 0
        for i in range(12):
            if(int(pre[i]) == -2):
                num+=1
        if(num>10):
            break
        for i in range(12):
            #print(i+2,pre[i])
            if(int(pre[i]) == -2):
                continue
            G.add_edge(i + 2, int(pre[i]))
        nx.draw_networkx(G, with_labels=True, pos=nodePos)
        for i in range(12,24):
            plt.text(x[i-12]+0.2,y[i-12],pre[i])
        plt.text(1,1, "round: "+pre[24])
        # plt.show()
        # break
        plt.savefig(delDir + '\\' + str(fignum) + ".svg", bbox_inches='tight', format = "svg")
        plt.close()
        linepre = line
        for i in range(12):
            if (int(pre[i]) == -2):
                continue
            G.remove_edge(i + 2, int(pre[i]))
        fignum += 1

#plt.show()
