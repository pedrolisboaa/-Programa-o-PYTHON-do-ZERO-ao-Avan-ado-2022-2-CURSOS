aluno = {'nome': 'Olívia', 'idade': 1, 'nota_final': 'A', 'aprovacao': True}

aluno['nome'] = 'Marcia'
aluno['idade'] = 15
aluno.update({'nota_final': 'A+', 'idade': 18})

print(aluno)
print(aluno.get('endereco', 'Valor não existe'))

del aluno['aprovacao']
print(aluno)