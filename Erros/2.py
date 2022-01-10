try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print(f'O valor deve ser um inteiro: ')
else:
    print(f'Produto cadastrado: ')
finally:
    print(f'Fim do programa!')
    print(f'Muito obrigado')