def calculate_value(result_from_arg, arg):

    value = result_from_arg[0][1]
    n = len(result_from_arg)

    #for i in result_from_arg:
    #    print(i)

    for i in range(n - 1):
        get_mult = 1
        for l in range(i + 1):
            get_mult *= (arg - result_from_arg[l][0])
        get_mult *= result_from_arg[i + 1][i + 2]
        value += get_mult

    return value


def interp(table, arg, func):
    result = []

    n = len(table)

    for i in range(n):
        L = []
        L.append(table[i][arg])
        L.append(table[i][func])
        for l in range(n - 1):
            L.append(0)
        result.append(L)

    for i in range(n - 1):
        for l in range(i + 1, n, 1):
            result[l][i + 2] = (result[l - 1][i + 1] - result[l][i + 1]) / (result[l - i - 1][0] - result[l][0])

    return result