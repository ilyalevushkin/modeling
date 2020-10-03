#d.update({"R"  : 0.35})
#    d.update({"L_e": 12})
#    d.update({"L_k": 187})
#    d.update({"C_k": 268})
#    d.update({"R_k": 0.25})
#    d.update({"U_c": 1400})
#    d.update({"I"  : 0.3})
#    time_mks = get_time_mks()
#    d.update({"Time": time_mks})
#    T_sigma = get_T_sigma()
#    d.update({"T_sigma": T_sigma})
#    I_T_0_m = get_I_T_0_m()
#    d.update({"I_T_0_m": I_T_0_m})

from interpolation import *

from math import *


def calc_temperature(t0, t_w, m, z):
    return t0 + (t_w - t0) * (z ** m)



def calc_integral_func(z, sigma_from_temperature, t_w, t0, m):
    return z * calculate_value(sigma_from_temperature, calc_temperature(t0, t_w, m, z))



def calc_integral_by_trap_method(sigma_from_temperature, t_w, t0, m):
    n, b, a = 1000, 1, 0
    h = (b - a) / n

    result = calc_integral_func(b, sigma_from_temperature, t_w, t0, m)

    a += h
    while (a < b):
        result += 2 * calc_integral_func(a, sigma_from_temperature, t_w, t0, m)
        a += h

    return result * h




def calc_r_p(l_e, r, sigma_from_temperature, t_w, t0, m):
    result = l_e / (2 * pi * r * r)
    result /= calc_integral_by_trap_method(sigma_from_temperature, t_w, t0, m)
    return result



def calc_f(i, u_c, r_k, l_k, r_p):
    return (u_c - (r_k + r_p) * i) / l_k
    #return u_c / l_k


def calc_phi(c_k, i):
    return -i / c_k

def calc_k_q_values(h_t, i, u_c, r_k, l_k, c_k, r_p):
    k, q = [], []
    k1 = h_t * calc_f(i, u_c, r_k, l_k, r_p)
    q1 = h_t * calc_phi(c_k, i)

    k2 = h_t * calc_f(i + k1 / 2, u_c + q1 / 2, r_k, l_k, r_p)
    q2 = h_t * calc_phi(c_k, i + k1 / 2)

    k3 = h_t * calc_f(i + k2 / 2, u_c + q2 / 2, r_k, l_k, r_p)
    q3 = h_t * calc_phi(c_k, i + k2 / 2)

    k4 = h_t * calc_f(i + k3, u_c + q3, r_k, l_k, r_p)
    q4 = h_t * calc_phi(c_k, i + k3)

    k.append(k1)
    k.append(k2)
    k.append(k3)
    k.append(k4)

    q.append(q1)
    q.append(q2)
    q.append(q3)
    q.append(q4)

    return k, q


def runge_kutta_part(k, y_n):
    return y_n + (k[0] + 2 * k[1] + 2 * k[2] + k[3]) / 6


def calc_runge_kutta_fourth(k, q, i, u_c):
    return runge_kutta_part(k, i), runge_kutta_part(q, u_c)


def calc_values(d):
    result = []
    u_c = d.get("U_c")
    i = d.get("I")
    time = d.get("Time")
    l_e = d.get("L_e")
    r = d.get("R")
    t_w = d.get("T_w")
    r_k = d.get("R_k")
    l_k = d.get("L_k")
    c_k = d.get("C_k")

    #интерполируем первую таблицу (формируем зависимость t0 от i и m от i)
    t0_from_i = interp(d.get("I_T_0_m"), 0, 1)
    m_from_i = interp(d.get("I_T_0_m"), 0, 2)

    #интерполируем вторую таблицу (формируем зависимость sigma от температуры)
    sigma_from_temperature = interp(d.get("T_sigma"), 0, 1)

    t0 = calculate_value(t0_from_i, log2(i))
    m = calculate_value(m_from_i, log2(i))

    r_p = calc_r_p(l_e, r, sigma_from_temperature, t_w, t0, m)


    result.append([u_c, i, t0, r_p, time[0]])


    for j in range(len(time) - 1):
        h_t = (time[j + 1] - time[j])

        k, q = calc_k_q_values(h_t, i, u_c, r_k, l_k, c_k, r_p)

        i, u_c = calc_runge_kutta_fourth(k, q, i, u_c)


        t0 = calculate_value(t0_from_i, log2(fabs(i)))
        m = calculate_value(m_from_i, log2(fabs(i)))
        r_p = calc_r_p(l_e, r, sigma_from_temperature, t_w, t0, m)

        result.append([u_c, i, t0, r_p, time[j + 1]])

    return result
