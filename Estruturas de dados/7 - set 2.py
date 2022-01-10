s1 = set(range(10))
print(s1)
s1.add(88)
s1.update([25, 36, 58 ])

print(s1)

set1 = {'a', 'b', 'c', 'd'}
set2 = {'e', 'f', 'g', 'h'}
set3 = {'i', 'j', 'l', 'k'}

set4 = set1.difference(set3)
print(set4)