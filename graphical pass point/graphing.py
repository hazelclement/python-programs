import matplotlib.pyplot as plt
import numpy as np
# values of x and y axes
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')


plt.xticks(np.arange(0, 51, 5))
plt.yticks(np.arange(0, 11, 1))
plt.show()