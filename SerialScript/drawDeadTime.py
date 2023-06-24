from matplotlib import pyplot as plt
import matplotlib
plt.figure(figsize=(8, 7), dpi=70)
matplotlib.rc("font",family='KaiTi')
x = [2,3,4]
x1 = [2.1,3.1,4.1]
x2 = [1.9,2.9,3.9]
y1 = [13204, 8798, 6747]
y2 = [8253, 8259, 7937]
x3 = [1.7, 4.3]
y3 = [6747, 6747]
y4 = [7939, 7939]
plt.bar(x1, y1, label='无能量均衡算法', width = 0.2)
plt.bar(x2, y2, label='有能量均衡算法', width = 0.2)
plt.plot(x3, y3, linestyle='--', c = 'b', label='网络故障开始时间')
plt.plot(x3, y4, linestyle='--', c = 'b')
plt.xticks(x, x)
plt.ylim(5000,13500)
plt.legend(loc="best")
plt.ylabel("生存时间/s",fontsize = 15)
plt.xlabel("节点ID",fontsize = 15)
plt.show()