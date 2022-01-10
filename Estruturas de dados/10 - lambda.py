def somar10(x):
    return x + 10


def eleva_quadrado_soma_10(x):
    func2 = lambda x: x ** 2
    return func2(x) + 10


# primeiro vem o nome lambda, depois o argumento, depois a expressão
somar = lambda x, y: x + y

print(somar10(2))
print(somar(2, 5))
print(eleva_quadrado_soma_10(10))
