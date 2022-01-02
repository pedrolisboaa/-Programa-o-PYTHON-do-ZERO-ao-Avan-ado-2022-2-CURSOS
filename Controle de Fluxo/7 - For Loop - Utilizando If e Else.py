compra_confirmada = True
dados_compra = 'Compra no valor de R$ 15.90 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para seu e-mail')
        break
else:
    print(f'Falha na compra')