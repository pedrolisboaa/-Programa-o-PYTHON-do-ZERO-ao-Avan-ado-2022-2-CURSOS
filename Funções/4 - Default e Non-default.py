def boas_vindas(nome='Senhor(a)', quantidade=0):
    print(f'Ola {nome}!')
    print(f'Temos {quantidade} carros, em estoque.')


boas_vindas('Pedro', 5)
print(f'------------------')
boas_vindas()
print(f'------------------')
boas_vindas()