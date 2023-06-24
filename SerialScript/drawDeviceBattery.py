import matplotlib.pyplot as plt
import matplotlib
from matplotlib import style
import random
from scipy import optimize
# style.use('ggplot')
#matplotlib.rcParams['text.usetex'] = True
plt.figure(figsize=(8, 7), dpi=70)
matplotlib.rc("font",family='KaiTi')
dir1 = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPLproject\OutputDeadDevice.txt"
dir2 = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPL2\OutputDeadDevice.txt"
with open(dir1) as f:
    lines = f.readlines()
    lines = lines[16:]
reNetworkingx = []
reNetworkingy = []
x = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
y = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
father = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
lastround = -1
lineshape = ['o', 'v', '1', 's', 'p', '*', 'h', '+', 'x', 'D', 'd','2']
continuenum = 20
for line in lines:
    value = [float(s) for s in line.split(',')]
    if(value[2] < 0.5):
        continuenum-=1
    if(continuenum ==0):
        break
    x[int(value[0])].append(value[3])
    y[int(value[0])].append(value[2])
    if(value[3] != lastround):
        reNetworkingx.append(value[3])
        reNetworkingy.append(value[2])
        father[int(value[0])].append(value[4])
    lastround = value[3]

for i in range(2, 14):
    plt.plot(x[i], y[i], label=str(i), marker = lineshape[i-2])
    #randpoint = random.randint(10, 20)
    plt.annotate(str(i), xy=(x[i][3], y[i][3]))
# for j in range(4, 15):
#     for i in range(len(reNetworkingx)):
#         plt.annotate("renetworking", xy=(reNetworkingx[i], reNetworkingy[i]))
# i = 12
# plt.scatter(x[i], y[i], label=str(i))
# for xy in zip(reNetworkingx, reNetworkingy):
#     plt.annotate('End Point', fontsize=20,
#                  xy=xy, xycoords='data',
#                  xytext=(0.8, 0.95), textcoords='axes fraction',
#                  arrowprops=dict(facecolor='black', shrink=0.1),
#                  horizontalalignment='right', verticalalignment='top')
plt.legend(loc="best")#, fontsize="large")
#plt.title(“中间节点剩余能量随轮次变化图“)
plt.ylabel("中间节点剩余能量/J",fontsize = 15)
plt.xlabel("轮次",fontsize = 15)
plt.show()