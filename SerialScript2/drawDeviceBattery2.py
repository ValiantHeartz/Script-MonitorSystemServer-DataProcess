import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import style
import random
from scipy import optimize
# style.use('ggplot')
#matplotlib.rcParams['text.usetex'] = True

plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置matplotlib整体用Times New Roman
plt.rcParams['font.weight'] = 'normal'  # 设置matplotlib整体用Times New Roman
plt.rcParams['font.size'] = 10.5  # 设置matplotlib整体用Times New Roman
plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

plt.figure(figsize=(8, 7), dpi=70)
protocol = 13
if protocol == 11:
    path = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPLproject\OutputTopology.txt"
    savepath = "C:/Users/zhoul/PycharmProjects/SerialScript2/WAMPLproject/nopower"
if protocol == 21:
    path = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPLproject\OutputTopology.txt"
    savepath = "C:/Users/zhoul/PycharmProjects/SerialScript2/WAMPLproject/withpower"
if protocol == 2:
    path = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPL2\OutputDeadDevice.txt"
    #savepath = "C:/Users/zhoul/PycharmProjects/SerialScript2/W/drawBattery"
if protocol == 13:
    path = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPL3-PeriodicBackward\OutputTopology.txt"
    savepath = "C:/Users/zhoul/PycharmProjects/SerialScript2/WAMPL3-PeriodicBackward/nopower"
if protocol == 23:
    path = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPL3-PeriodicBackward\OutputTopology.txt"
    savepath = "C:/Users/zhoul/PycharmProjects/SerialScript2/WAMPL3-PeriodicBackward/withpower"
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
    if int(preround) == 25: break  ## have energy
    # if int(preround) == 16: break
    for i in range(0, 12):
        x[i].append(preround)
        y[i].append(line[i])
for i in range(0, 12):
    plt.plot(x[i], y[i], label=str(i+2), marker = lineshape[i],color = 'black', linestyle='dashed')
    plt.ylim([0,3.5])
    #randpoint = random.randint(10, 20)
    #plt.annotate(str(i), xy=(x[i][3], y[i][3]))
    j = 1
    if i == 4:
        while j < 22:
            # print(y[i][j])
            j+=1

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

mpl.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置matplotlib整体用Times New Roman
# mpl.rcParams['font.weight'] = 'bold'  # 设置matplotlib整体用Times New Roman
# mpl.rcParams['font.size'] = 10.5  # 设置matplotlib整体用Times New Roman

plt.legend(loc="best")#, fontsize="large")
#plt.title(“中间节点剩余能量随轮次变化图“)
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 10.5,
         }
plt.ylabel("Remaining energy/J", font1)
plt.xlabel("Round", font1)
plt.savefig(savepath + '\\' + "中间节点剩余能量随轮次变化图"+ (str)(protocol) + ".svg", bbox_inches='tight', format = "svg")
plt.show()
plt.show()