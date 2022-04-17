import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

# 设置线条粗细
ax.scatter(x_values, y_values, c='red' ,s  = 10)

ax.set_title("xx", fontsize=24)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

ax.axis([0, 1100, 0, 1100000])

# 显示图标
# plt.show()

# 保存到文件
plt.savefig('squares_plot.png')