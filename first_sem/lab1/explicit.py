#явный
#взята функция u'(x) = x^2 + u^2(x)

def explicit(ksi, eta, h, x_finish):
    while (ksi < x_finish):
        eta = eta + h * (eta ** 2 + ksi ** 2)
        ksi += h
        #print(ksi, " : ", eta)
    return eta
