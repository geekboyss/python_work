import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

# 创建图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s = 10)

# 设置图标和坐标轴名称
ax.set_title("Cubes", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

# 设置刻度标签大小及每个坐标的取值范围
ax.tick_params(axis='both', labelsize = 14)
ax.axis([0, 5100, 0, 5100**3])

# 显示图像
plt.show()  