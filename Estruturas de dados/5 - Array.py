from array import array

letras = ['a', 'b', 'c', 'd', 'e']
numero_i = [1, 2, 3, 4, 5]
numero_f = [1.1, 2.2, 3.3, 4.4, 5.5]

print(letras)
print(numero_i)
print(numero_f)
print()

letras = array('u', letras)
numero_i = array('i', numero_i)
numero_f = array('f', numero_f)

print(letras)
print(numero_i)
print(numero_f)