import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)

plt.plot(x, x, label='linear') # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic') # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x_label')
plt.ylabel('y_label')
plt.title("Simple_Plot")
plt.legend()
plt.show()