s = 'a'
t = 'b'

s + t = 'ab'
(d)

s * t = TypeError
(e)

s * 6 = aaaaaa
(d)

s[0] = 'a'
s[len(s) - 1] = 'a'

Given
s = 'm'
s = 'c'

1. value of s is c

s = 'n'
s[0] = 'c'

2. value of s is n

s = ''
len(s) = 0

Given
s = 'silence' #7 chars
t = 'everyone' #8 chars

A) s[len(s)] = IndexError: string index is out of range
B) s[len(s) - 2] = 'c'
C) s[-2] = 'c'
D) s[-5:-2] = 'len'
E) s[-2:-5] = '' #predict cne, actual ''
F) s[-2:-2] = ''
G) s[0:len(s):2] = 'slne'
H) s[::-1] = 'ecnelis'
I) s[::-2] = 'enls'
J) s+t[4:6] = 'silenceyo'
K) (s+t)[4:6] = 'nc'