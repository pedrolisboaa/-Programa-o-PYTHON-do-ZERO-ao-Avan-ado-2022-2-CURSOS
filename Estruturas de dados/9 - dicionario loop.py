aluno = {'nome': 'Olívia', 'idade': 1, 'nota_final': 'A', 'aprovacao': True}

for x in aluno.items():
    print(x)

for n in aluno.keys():
    print(n)

for x in aluno.values():
    print(x)

for keys, values in aluno.items():
    print(f'{keys} - {values}')

aluno2 = {'nome': 'Olívia',
          'idade': 1,
          'nota_final': 'A',
          'aprovacao': True,
          'materias': ['portugues', 'matematica', 'biologia']}

print(aluno2)
print(aluno2.get('materias'))
