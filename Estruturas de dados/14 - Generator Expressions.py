from sys import getsizeof
numeros = [x * 10 for x in range(100_000_000)]
print(type(numeros))
print(getsizeof(numeros))


#print(numeros)

numeros2 = (x * 10 for x in range(100_000_000))
print(type(numeros2))
print(getsizeof(numeros2))