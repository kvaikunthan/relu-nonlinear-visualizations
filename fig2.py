import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 400)

w1, b1 = 1.4, 0.5
m = w1 * x + b1

w2, b2 = 0.5, 1.2
n = w2 * m + b2


plt.plot(x, n, color='blue')
plt.title('Only weights and biases')
plt.xlabel('x')
plt.ylabel('n')
plt.grid()
plt.show()