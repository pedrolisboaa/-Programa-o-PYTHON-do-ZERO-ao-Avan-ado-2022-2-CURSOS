def cliente1(nome):
    print(f'Olá {nome}!')


def cliente2(nome):
    return f'Ola {nome}!'


cliente = cliente2('Juliana')
cliente1('Juliana')
print(cliente)
