import matplotlib.pyplot as plt
import numpy as np

def draw_result(func, x_0, x_N, h):

    arg = [i for i in np.arange(x_0, x_N + h, h)]

    x = np.array(arg)
    y = np.array(func)

    plt.plot(x, y)

    plt.ylabel("T, К")
    plt.xlabel("x, см")

    plt.grid(True)

    plt.show()