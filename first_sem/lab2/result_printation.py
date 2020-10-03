import matplotlib.pyplot as plt
import numpy as np

def get_column(mas, i):
    L = []
    for j in range(len(mas)):
        L.append(mas[j][i])
    return L

def list_multy(lst1, lst2):
    L = []
    for j in range(len(lst1)):
        L.append(lst1[j] * lst2[j])
    return L


def print_graphic(result, i, str, ax):

    x = np.array(get_column(result, 4))
    y = np.array(get_column(result, i))

    ax.plot(x, y)

    ax.set_ylabel(str)
    ax.set_xlabel('t')

    ax.grid(True)

def print_last_graphic(result, str, ax):
    x = np.array(get_column(result, 4))
    y = np.array( list_multy(get_column(result, 3), get_column(result, 1)) )

    ax.plot(x, y)

    ax.set_ylabel(str)
    ax.set_xlabel('t')

    ax.grid(True)


def print_results(result):
    k = len(result)
    fig, ax = plt.subplots(nrows = 3, ncols = 2)

    print_graphic(result, 0, 'U_c(t)', ax[0][0])

    print_graphic(result, 1, 'I(t)', ax[0][1])

    print_graphic(result, 2, 'T0(t)', ax[1][0])

    print_graphic(result, 3, 'R_p(t)', ax[1][1])

    print_last_graphic(result, 'IR_p(t)', ax[2][0])

    plt.show()