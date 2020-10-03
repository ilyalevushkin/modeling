from progonka import *

def calc_const(k_0, k_N, x_N, x_0):
    b = (k_N * x_N - x_0 * k_0) / (k_N - k_0)
    a = k_0 * (x_0 - b)
    return a, b

def calc_a_b_c_d(k_0, k_N, alpha_0, alpha_N, x_N, x_0):
    a, b = calc_const(k_0, k_N, x_N, x_0)
    c, d = calc_const(alpha_0, alpha_N, x_N, x_0)
    return a, b, c, d


def alpha(c, d, x):
    return c / (x - d)

def k(a, b, x):
    return a / (x - b)

def f(T_0, R, c, d, x):
    return 2.0 * T_0 / R * alpha(c, d, x)

def p(c, d, R, x):
    return 2.0 / R * alpha(c, d, x)

#метод трапеций
def X_n_plus_half(k_n, k_n_plus_1):
    return 2.0 * k_n * k_n_plus_1 / (k_n + k_n_plus_1)

def A_n(a, b, h, x):
    return X_n_plus_half(k(a, b, x), k(a, b, x - h)) / h

def C_n(a, b, h, x):
    return X_n_plus_half(k(a, b, x), k(a, b, x + h)) / h

def B_n(a, b, h, c, d, R, x):
    return A_n(a, b, h, x) + C_n(a, b, h, x) + p(c, d, R, x) * h

def F_n(T_0, R, c, d, h, x):
    return f(T_0, R, c, d, x) * h

def solve_task(const, x_0, x_N, h):

    k_0 = const.get("k_0")
    k_N = const.get("k_N")
    alpha_0 = const.get("alpha_0")
    alpha_N = const.get("alpha_N")
    F_0 = const.get("F_0")
    T_0 = const.get("T_0")
    R = const.get("R")


    a, b, c, d = calc_a_b_c_d(k_0, k_N, alpha_0, alpha_N, x_N, x_0)

    #вариант с обнулением h^2
    K_0 = 1
    M_0 = -1
    X_half = X_n_plus_half(k_0, k(a, b, x_0 + h))
    P_0 = h * F_0 / X_half

    K_N = 1
    X_n_minus_half = X_n_plus_half(k_N, k(a, b, x_N - h))
    znam = alpha(c, d, x_N) * h + X_n_minus_half
    M_N = -1 * X_n_minus_half / znam
    P_N = h * alpha(c, d, x_N) * T_0 / znam

    #вариант без обнуления h^2
    '''K_0 = 1
    X_half = X_n_plus_half(k_0, k(a, b, x_0 + h))
    temp1 = 0.5 * (p(c, d, R, x_0) + p(c, d, R, x_0 + h))
    znam1 = X_half + h * h / 8 * temp1 + h * h / 4 * p(c, d, R, x_0)
    M_0 = (h * h / 8 * temp1 - X_half) / znam1
    temp3 = h * h / 4 * (1.5 * f(T_0, R, c, d, x_0) + 0.5 * f(T_0, R, c, d, x_0 + h))
    P_0 = (h * F_0 + temp3) / znam1

    K_N = 1
    X_N_minus_half = X_n_plus_half(k_N, k(a, b, x_N - h))
    temp2 = h * h / 8 * 0.5 * (p(c, d, R, x_N) + p(c, d, R, x_N - h))
    alp = alpha(c, d, x_N)
    znam2 = alp * h + temp2 + h * h / 4 * p(c, d, R, x_N) + X_N_minus_half
    M_N = (temp2 - X_N_minus_half) / znam2
    P_N = (h * alp * T_0 + temp3) / znam2'''

    return progonka(A_n, B_n, C_n, F_n,
                    K_0, M_0, P_0,
                    K_N, M_N, P_N,
                    x_0, h, x_N, a, b, c, d, T_0, R)
