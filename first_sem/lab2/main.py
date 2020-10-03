from calculations import *
from result_printation import *
from math import *
import numpy as np

def get_time_mks(a, b, h):
    return [i for i in np.arange(a * 10e-7, b * 10e-7, h * 10e-7)]

def get_T_sigma():
    return [[2000, 0.525e-3],
            [3000, 0.525e-2],
            [4000, 0.031],
            [5000, 0.27],
            [6000, 2.05],
            [7000, 6.06],
            [8000, 12.0],
            [9000, 19.9],
            [10000, 29.6],
            [11000, 41.1],
            [12000, 54.1],
            [13000, 67.7],
            [14000, 81.5]]

def get_I_T_0_m():
    return [[log2(0.5), 6400, 0.4],
            [log2(1), 6790, 0.55],
            [log2(5), 7150, 1.7],
            [log2(10), 7270, 3],
            [log2(50), 8010, 11],
            [log2(200), 9185, 32],
            [log2(400), 10010, 40],
            [log2(800), 11140, 41],
            [log2(1200), 12010, 39]]

def get_default_constants(d):
    d.update({"R"  : 0.35})
    d.update({"L_e": 12.0})
    d.update({"L_k": 187e-6})
    d.update({"C_k": 268e-6})
    d.update({"R_k": 0.25})
    d.update({"U_c": 1400.0})
    d.update({"I"  : 0.5})
    d.update({"T_w": 2000.0})
    d.update({"Time_from (mksec)": 0})
    d.update({"Time_to (mksec)": 10000})
    d.update({"Time_h (mksec)": 10})
    T_sigma = get_T_sigma()
    d.update({"T_sigma": T_sigma})
    I_T_0_m = get_I_T_0_m()
    d.update({"I_T_0_m": I_T_0_m})


def print_constants(d):
    L = d.items()

    k = 0
    for key, value in L:
        if (k < len(L) - 2):
            print(key, value)
        k += 1


def print_menu():
    print("Выберите параметр для изменения:")
    print("1.L_k")
    print("2.C_k")
    print("3.R_k")
    print("4.U_c0")
    print("5.I_0")
    print("6.Time_from")
    print("7.Time_to")
    print("8.Time_h")
    print("9.Распечатать значения")
    print("0.Настройка завершена")

def change_value(d, choice):
    if (choice == 1):
        value = float(input("Введите новый L_k:"))
        d.update({"L_k": value})
    elif (choice == 2):
        value = float(input("Введите новый C_k:"))
        d.update({"C_k": value})
    elif (choice == 3):
        value = float(input("Введите новый R_k:"))
        d.update({"R_k": value})
    elif (choice == 4):
        value = float(input("Введите новый U_c0:"))
        d.update({"U_c": value})
    elif (choice == 5):
        value = float(input("Введите новый I_0:"))
        d.update({"I": value})
    elif (choice == 6):
        value = float(input("Введите новый Time_from (mksec):"))
        d.update({"Time_from (mksec)": value})
    elif (choice == 7):
        value = float(input("Введите новый Time_to (mksec):"))
        d.update({"Time_to (mksec)": value})
    elif (choice == 8):
        value = float(input("Введите новый Time_h (mksec):"))
        d.update({"Time_h (mksec)": value})


def get_constants():
    d = {}
    get_default_constants(d)
    print_constants(d)
    while (True):
        print_menu()
        choice = int(input())
        if (choice == 0):
            break
        elif (choice == 9):
            print_constants(d)
        elif (choice < 9 and choice > 0):
            change_value(d, choice)

    time_mks = get_time_mks(d.get("Time_from (mksec)"), d.get("Time_to (mksec)"), d.get("Time_h (mksec)"))
    d.update({"Time": time_mks})
    return d



def get_array(L_test, t0_from_i):
    result = []
    for i in L_test:
        result.append(calculate_value(t0_from_i, log2(i)))
    return result


if __name__ == '__main__':
    d = get_constants()

    result = calc_values(d)

    print_results(result)


