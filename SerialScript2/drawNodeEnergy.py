import networkx as nx
import matplotlib.pyplot as plt
import array
import os
import numpy as np
import matplotlib as mpl

plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 设置matplotlib整体用Times New Roman
plt.rcParams['font.weight'] = 'normal'  # 设置matplotlib整体用Times New Roman
plt.rcParams['font.size'] = 10.5  # 设置matplotlib整体用Times New Roman
plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

protocol = 3
dir1 = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPLproject\OutputDead.txt"
# savepath = "C:/Users/zhoul/PycharmProjects/SerialScript2/WAMPL3-PeriodicBackward/drawNodeEnergy"

dir3 = "D:\OMNET\omnetpp-6.0-windows-x86_64\omnetpp-6.0\samples\WAMPL3-PeriodicBackward\OutputDead.txt"
savepath = "C:/Users/zhoul/PycharmProjects/SerialScript2"

x_label = [2,3,4,5,6,7,8,9,10,11,12,13]
y1 = []
y3 = []
length = len(x_label)
x = np.arange(length)
total_width, n = 0.8, 2   # 柱状图总宽度，有几组数据
width = total_width / n
x1 = x - width / 2  # 第一组数据柱状图横坐标起始位置
x3 = x1 + width  # 第二组数据柱状图横坐标起始位置
with open(dir1) as f:
    lines1 = f.readlines()
with open(dir3) as f:
    lines3 = f.readlines()
energy1=lines1[2].split(',')
energy3=lines3[2].split(',')
for i in range(len(x)):
    y1.append(float(energy1[i]))
    y3.append(float(energy3[i]))
    # print(energy1[i])

plt.bar(x1, y1, width=width, label='Forward Networking Algorithm',color="#000000")
plt.bar(x3, y3, width=width, label='Backward Equalization algorithm',color="#808080")
plt.legend()
plt.xticks(x, x_label)   # 用星期几替换横坐标x的值
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 10.5,
         }
plt.ylabel("Remaining energy/J", font1)
plt.xlabel("Node", font1)
plt.savefig(savepath + '\\' + "drawNodeEnergy" + ".svg", bbox_inches='tight', format = "svg")
plt.show()
plt.close()