def soma(*args):
    total = 0
    for n in args:
        total += n
    return total


teste = soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(teste)
