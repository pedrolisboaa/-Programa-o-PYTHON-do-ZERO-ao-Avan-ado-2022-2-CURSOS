lista = list(range(10))
lista1 = map(lambda x: x * 2, lista)
print(list(lista1))


def upper(x):
    return x.upper()


nome = ['pedro', 'juliana', 'olivia']
nome_upper = map(upper, nome)
print(list(nome_upper))

print(list(map(lambda x: x.upper(), nome)))
print(list(map(lambda x: x**2, list(range(10)))))