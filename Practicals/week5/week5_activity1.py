from typing import List

names = ['Bob', 'Ho', 'Zahara', 'Amitabha', 'Dov', 'Maria']
print(names[2:5])
print(names[0:1])
print(names[3:])

names.remove('Ho')
print(names)

x = ['I am well']
x.insert(0, 'How are you?')
print(x)

x = [2, 4, 99, 0, -3.5, 86.9, -101]
x.sort()
x.reverse()
print(x)

def every_third(L: List[str]) -> List[str]:
    count = 2
    acc = []
    for i in range(len(L)):
        count += 1
        if count == 3:
            acc.append(L[i])
            count = 0
    return acc

def every_ith(L: List[str], i: int) -> List[str]:
    count = i-1
    acc = []
    for item in range(len(L)):
        count += 1
        if count == i:
            acc.append(L[item])
            count = 0
    return acc

def every_third_revisited(L: List[str]) -> List[str]:
    return every_ith(L, 3)