import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s = 3)

ax.set_title("Cubes", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

ax.tick_params(axis='both', labelsize = 14)
ax.axis([0, 5100, 0, 5100**3])
plt.show()  