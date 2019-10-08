s = 'superconductivity'

for i in s:
    print(i)


acc = ''
for i in s:
    acc = f'{acc}{i} '
acc = acc[0:-1]
print(acc)


s = 'parsimonious'
for index in range(len(s)):
    print(f'{s[index]} {index}')


for index in range(len(s)):
    if index % 2 == 0:
        print(s[index])

