import datetime

import numpy as np
import matplotlib.pyplot as plt
# import matplotlib as mpl
plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置matplotlib整体用Times New Roman
plt.rcParams['font.weight'] = 'bold'  # 设置matplotlib整体用Times New Roman
plt.rcParams['font.size'] = 10.5  # 设置matplotlib整体用Times New Roman
plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
lineshape = ['o', 'v', '1', 's', 'p', '*', 'h', '+', 'x', 'D', 'd','2']
datanum = 30

data = np.zeros((5,datanum), dtype=int)
battery = np.zeros((5,datanum), dtype=int)
rssi = np.zeros((5,datanum), dtype=int)
snr = np.zeros((5,datanum), dtype=int)
dir = "C:/Users/zhoul/PycharmProjects/LoRaWANHttpServer/LoRaWANData/03 03 10-13 LoRaWANData.txt"
savepath = "C:/Users/zhoul/PycharmProjects/SerialScript2"
with open(dir) as f:
    lines = f.readlines()

for line in lines:
    macPayload = line.split(',')[13:]
    print(macPayload)
    if(int(line[1]) < datanum+4):
        for i in range(11):
            if (i * 10 < len(macPayload) and int(macPayload[i * 10+1]) < datanum):
                # if(int(macPayload[i * 10])-1 < 5):
                print(macPayload[i*10:(i+1)*10])
                id=int(macPayload[i * 10])
                dataid=int(macPayload[i * 10+1])
                data[id-1][dataid-1] -= 1
                rssi[id-1][dataid-1] = int(macPayload[i * 10 + 3])
                snr[id - 1][dataid - 1] = int(macPayload[i * 10 + 4])
            else:
                break
dataReceiceRate = np.zeros(5, dtype=float)
dataLossRate = np.zeros(5, dtype=float)
signalNum = datanum
for i in range(5):
    dataReceive = 0
    dataLoss = 0
    for j in range(datanum):
        if(data[i][j] != 0):
            dataReceive += 1
            dataLoss  += -data[i][j] - 1
            signalNum += -data[i][j] - 1
        else:
            dataLoss += 1
    dataReceiceRate[i] = dataReceive/datanum
    dataLossRate[i] = dataLoss/datanum
    print("节点: ",i)
    print("dataReceiceRate: ", dataReceiceRate[i])
    print("dataLossRate: ", dataLossRate[i])


# plt.ylim([0,0.35])
for i in range(3):
    plt.plot(range(datanum), rssi[i+2]-150-130, marker = lineshape[i], linestyle='dashed', color = 'black',label = i+3)

plt.legend(loc="lower right")#, fontsize="large")

#plt.title(“中间节点剩余能量随轮次变化图“)
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 10.5,
         }
plt.ylabel("RSSI", font1)
plt.xlabel("Upload Cycle", font1)

plt.ylim(-170,-120)

plt.savefig(savepath + '\\' + "systemAnalysis" + ".svg", bbox_inches='tight', format = "svg")

plt.show()

