valores = [11, 25, 36, 89, 53, 15, 22]


def remover_20(x):
    return x > 20


print(list(filter(remover_20, valores)))