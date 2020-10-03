#взята функция u'(x) = x^2 + u^2(x)

class Element(object):
    def __init__(self, koef, exp):
        self.koef = koef
        self.exp = exp



def get_the_result_from_polynom(polynom, x):
    res = 0
    for i in polynom:
        buf = i.koef
        for j in range(i.exp):
            buf *= x
        res += buf

    return res

def add_element_to_polynom(polynom, element):
    flag = False
    for i in range(len(polynom)):
        if (polynom[i].exp == element.exp):
            polynom[i].koef = polynom[i].koef + element.koef
            flag = True
            break

    if (flag == False):
        polynom.append(element)

    return polynom

def get_double_multy(polynom):
    result = []
    if (len(polynom) == 0):
        return result

    for k in range(len(polynom) - 1):
        p = 2 * polynom[k].koef
        er = polynom[k].exp
        for i in range(k + 1, len(polynom)):
            koef = p * polynom[i].koef
            exp = er + polynom[i].exp
            element = Element(koef, exp)
            result.append(element)

    return result


def square_polynom(polynom):
    new_polynom = []
    for i in range(len(polynom)):
        element = Element(polynom[i].koef ** 2, polynom[i].exp * 2)
        new_polynom.append(element)

    double_multy = get_double_multy(polynom)

    for i in range(len(double_multy)):
        new_polynom = add_element_to_polynom(new_polynom, double_multy[i])

    return new_polynom

def get_antiderivative(polynom):

    for i in range(len(polynom)):
        polynom[i].exp = polynom[i].exp + 1
        polynom[i].koef = polynom[i].koef / polynom[i].exp

    return polynom

def substitution(polynom, ksi):


    element = Element(-1 * get_the_result_from_polynom(polynom, ksi), 0)

    polynom = add_element_to_polynom(polynom, element)

    return polynom

def calc_integral(ksi, polynom):
    polynom = square_polynom(polynom)

    element = Element(1, 2)

    polynom = add_element_to_polynom(polynom, element)

    polynom = get_antiderivative(polynom)

    polynom = substitution(polynom, ksi)

    return polynom

def calculate_iter_polynom(ksi, eta, polynom):
    polynom = calc_integral(ksi, polynom)

    element = Element(eta, 0)

    polynom = add_element_to_polynom(polynom, element)

    return polynom


def pikar(ksi, eta, p):
    polynom = []

    first = Element(eta, 0)
    polynom.append(first)

    for i in range(p):
       polynom = calculate_iter_polynom(ksi, eta, polynom)

    #for i in range(len(polynom)):
    #    print(str(polynom[i].koef) + "x^" + str(polynom[i].exp), end = ' + ')

    return polynom