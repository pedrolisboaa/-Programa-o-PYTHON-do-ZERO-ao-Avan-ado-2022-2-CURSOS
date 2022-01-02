preco_produto = float(input('Infome o preço do produto: '))

while preco_produto >= 20:
    comissao = preco_produto * 0.1
    print(f'Um produto de R${preco_produto:.2f} paga R${comissao:.2f} de comissão.')
    break
else:
    print(f'Um produto de R${preco_produto:.2f} não paga comissão.')