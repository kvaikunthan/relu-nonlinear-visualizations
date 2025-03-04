import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

x = np.linspace(-5, 5, 400)

plt.figure(figsize=(7, 5))

plt.plot(x, sigmoid(x), color='blue')
plt.title('Sigmoid Function')
plt.grid()
plt.xlabel('x')
plt.ylabel('sigmoid(x)')
plt.show()

plt.plot(x, relu(x), color='red')
plt.title('ReLU Function')
plt.grid()
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.show()