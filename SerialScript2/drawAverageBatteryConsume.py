import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import style
import random
from scipy import optimize
# style.use('ggplot')
#matplotlib.rcParams['text.usetex'] = True

plt.figure(figsize=(8, 7), dpi=70)
protocol = 1
if protocol == 1:
    path = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPLproject\OutputTopology.txt"
if protocol == 2:
    path = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPL2\OutputDeadDevice.txt"
if protocol == 3:
    path = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPL3-PeriodicBackward\OutputTopology.txt"
savepath = "C:/Users/zhoul/PycharmProjects/SerialScript2"
with open(path) as f:
    lines = f.readlines()
    # lines = lines[12:]
reNetworkingx = []
reNetworkingy = []
x = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
y = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
father = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
lastround = -1
lineshape = ['o', 'v', '1', 's', 'p', '*', 'h', '+', 'x', 'D', 'd','2']
continuenum = 60
countstart = 0
# for line in lines:
#     value = [float(s) for s in line.split(',')]
#     if(value[2] < 0.2):
#         countstart = 1
#     if(countstart == 1):
#         continuenum-=1
#     if(continuenum ==0):
#         break
#     x[int(value[0])].append(value[3])
#     y[int(value[0])].append(value[2])
#     if(value[3] != lastround):
#         reNetworkingx.append(value[3])
#         reNetworkingy.append(value[2])
#         father[int(value[0])].append(value[4])
#     lastround = value[3]
#     # if len(x[0]) > 16:
#     #     break

preround = 0
for line in lines:
    line = line[0:len(line)-2]
    line = [float(s) for s in line.split(',')]
    line = line[12:]
    if line[12] == preround:
        continue
    preround = line[12]
    # if int(preround) == 62: break  ## have energy
    if int(preround) == 16: break
    for i in range(0, 12):
        x[i].append(preround)
        y[i].append(line[i])
y_average = []
x_average = []
for i in range(0, 12):
    x_average.append(i+2)
    # print(y[i][0:10])
    # break
    consume = 0
    for j in range(1,10):
        consume += y[i][j-1] - y[i][j]
    y_average.append(consume/10)
    # plt.plot(x[i], y[i], label=str(i+2), marker = lineshape[i])
    # plt.ylim([0,3.5])
plt.ylim([0,0.35])
plt.plot(x_average, y_average)

mpl.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置matplotlib整体用Times New Roman
# mpl.rcParams['font.weight'] = 'bold'  # 设置matplotlib整体用Times New Roman
# mpl.rcParams['font.size'] = 10.5  # 设置matplotlib整体用Times New Roman

plt.legend(loc="best")#, fontsize="large")
#plt.title(“中间节点剩余能量随轮次变化图“)
fontsize = 15
plt.ylabel("Average energy consumption/J", fontsize=fontsize)
plt.xlabel("Node", fontsize=fontsize)
plt.savefig(savepath + '\\' + "drawAverageBatteryConsume"+ (str)(protocol) + ".svg", bbox_inches='tight', format = "svg")
plt.close()
plt.show()