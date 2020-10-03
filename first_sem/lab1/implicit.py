from math import sqrt
#неявный
#взята функция u'(x) = x^2 + u^2(x)

def implicit(ksi, eta, h, x_finish):
    try:
        while (ksi < x_finish):
            eta = 1 - sqrt(1 - 4 * h * (h * ((ksi + h) ** 2) + eta))
            eta /= 2 * h
            ksi += h
    except:
        eta = 0
    return eta
