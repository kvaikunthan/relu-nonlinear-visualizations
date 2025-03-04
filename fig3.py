import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-5, 5, 400)[None, :]  # Shape: (1, 400)



plt.plot(x.flatten(), sigmoid(n), color='blue')
plt.title('With Sigmoid')
plt.xlabel('x')
plt.ylabel('sigmoid(n)')
plt.grid()
plt.show()
