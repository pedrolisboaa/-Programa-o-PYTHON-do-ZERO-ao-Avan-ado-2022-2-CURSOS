produtos = ['arroz', 'feijão', 'laranja', 'banana']
item1, item2, *item3 = produtos

print(item1)
print(item2)
print(item3)

valores = [50, 80, 110, 150, 220]

for n, i in enumerate(valores):
    print(f'O preço do produto {n+1} é R$ {i:.2f}')

cor = input('informe uma cor: ').lower().strip()
lista_cores = ['amarelo', 'verde', 'azul', ' vermelho']
if cor in lista_cores:
    print(f'Sim')
else:
    print('Não')