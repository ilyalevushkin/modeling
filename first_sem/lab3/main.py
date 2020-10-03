from print_graph import *
from task import *


def fill_base_constants():
    const = {}

    const.update({"k_0": 0.4})
    const.update({"k_N": 0.1})
    const.update({"alpha_0": 0.05})
    const.update({"alpha_N": 0.01})
    const.update({"l": 10.0})
    const.update({"T_0": 300.0})
    const.update({"R": 0.5})
    const.update({"F_0": 132.994})

    return const


def print_constants(const):
    for key, value in const.items():
        print(key, ":", value)


def print_menu():
    print("Выберите действие: ")
    print("1. Сменить k_0")
    print("2. Сменить k_N")
    print("3. Сменить alpha_0")
    print("4. Сменить alpha_N")
    print("0. Настройка завершена")
    return int(input())


def change_value(const, str):
    new_value = float(input("Введите " + str + ": "))
    const.update({str: new_value})

if __name__ == '__main__':
    const = fill_base_constants()

    while(True):
        print_constants(const)

        choice = print_menu()

        if (choice == 0):
            break
        elif (choice == 1):
            change_value(const, "k_0")
        elif (choice == 2):
            change_value(const, "k_N")
        elif (choice == 3):
            change_value(const, "alpha_0")
        elif (choice == 4):
            change_value(const, "alpha_N")

    x_0 = 0

    x_N = const.get("l")

    h = float(input("Введите шаг: "))

    result = solve_task(const, x_0, x_N, h)

    #print(result)

    draw_result(result, x_0, x_N, h)