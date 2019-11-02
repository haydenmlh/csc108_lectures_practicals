x = open('data1.txt')
i = 0
x.close()

#Run 11 times to read the end of file
#shows ''


x = open('data1.txt')

for i in x:
    print(i)

x.close()
print('end of x')

y = open('data2.txt')

for i in y:
    if 'lol' in i.lower():
        print(i, end='')

y.close()

y = open('data2.txt')
z = open('output.txt', 'w')
for i in y:
    if 'lol' in i.lower():
        z.write(i)
y.close()
z.close()