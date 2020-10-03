from pikar import *
from explicit import *
from prettytable import PrettyTable
from implicit import *


def create_x_values(x_from, h, count):
    L = []
    for i in range(count):
        L.append(x_from)
        x_from += h
    return L

ksi = float(input("Введите кси: "))
eta = float(input("Введите этта: "))

p1 = int(input("Введите количество итераций для метода Пикара (p1): "))
p2 = int(input("Введите количество итераций для метода Пикара (p2): "))
p3 = int(input("Введите количество итераций для метода Пикара (p3): "))

h = float(input("Введите шаг для численных методов: "))

x_h = float(input("Введите шаг для x: "))

x_count = int(input("Введите количество x: "))

x_values = create_x_values(ksi, x_h, x_count)

pikar_p1_values = []
pikar_p2_values = []
pikar_p3_values = []
explicit_values = []
implicit_values = []

polynom_p1 = pikar(ksi, eta, p1)
polynom_p2 = pikar(ksi, eta, p2)
polynom_p3 = pikar(ksi, eta, p3)


explicit_values.append(0)
implicit_values.append(0)

for i in range(len(x_values)):
    pikar_p1_values.append(get_the_result_from_polynom(polynom_p1, x_values[i]))
    pikar_p2_values.append(get_the_result_from_polynom(polynom_p2, x_values[i]))
    pikar_p3_values.append(get_the_result_from_polynom(polynom_p3, x_values[i]))

    if (i == len(x_values) - 1):
        break
    explicit_values.append(explicit(x_values[i], explicit_values[len(explicit_values) - 1], h, x_values[i] + x_h))
    implicit_values.append(implicit(x_values[i], implicit_values[len(implicit_values) - 1], h, x_values[i] + x_h))

#for i in explicit_values:
#    print(i)

#print()

#for i in implicit_values:
#    print(i)


x = PrettyTable()

x.field_names = ["x", "p = " + str(p1), "p = " + str(p2), "p = " + str(p3), "Явно, шаг : " + str(h), "Неявно"]

for i in range(len(x_values)):
    x.add_row(["{:8.2f}".format(x_values[i]), pikar_p1_values[i], pikar_p2_values[i],
               pikar_p3_values[i], explicit_values[i], implicit_values[i]])

print(x)