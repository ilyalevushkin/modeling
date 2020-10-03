

def calc_n_plus_1_ksi(ksi_n, C_n, B_n, A_n, x, a, b, c, d, R, h):
    return C_n(a, b, h, x) / (B_n(a, b, h, c, d, R, x) - A_n(a, b, h, x) * ksi_n)

def calc_n_plus_1_etta(ksi_n, etta_n, B_n, A_n, x, F_n, a, b, c, d, T_0, R, h):
    return (F_n(T_0, R, c, d, h, x) + A_n(a, b, h, x) * etta_n) / (B_n(a, b, h, c, d, R, x) - A_n(a, b, h, x) * ksi_n)


def calc_y_n(ksi_n_plus_1, etta_plus_1, y_plus_1):
    return ksi_n_plus_1 * y_plus_1 + etta_plus_1

def progonka(A_n, B_n, C_n, F_n, K_0, M_0, P_0, K_N, M_N, P_N, x_0, h, x_N, a, b, c, d, T_0, R):

    ksi = []
    etta = []
    y_result = []

    #начальные кси и этта
    ksi_1 = -M_0 / K_0
    etta_1 = P_0 / K_0

    ksi.append(ksi_1)
    etta.append(etta_1)

    #вычисление всех кси и этта
    i = 0
    x_0 += h
    while (x_0 < (x_N - h)):
        ksi.append(calc_n_plus_1_ksi(ksi[i], C_n, B_n, A_n, x_0, a, b, c, d, R, h))
        etta.append(calc_n_plus_1_etta(ksi[i], etta[i], B_n, A_n, x_0, F_n, a, b, c, d, T_0, R, h))
        x_0 += h
        i += 1


    #вычисление y_N
    y_N = (P_N - M_N * etta[i]) / (K_N + M_N * ksi[i])

    y_result.append(y_N)

    #вычислене всех y_n
    for i in range(len(ksi) - 1, -1, -1):
        y_result.append(calc_y_n(ksi[i], etta[i], y_result[-1]))

    y_result.reverse()

    return y_result