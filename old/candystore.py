#https://open.kattis.com/contests/sat25v/problems/candystore
n, q = input().split()
initials = {}
for i in range(int(n)):
    name = input()
    #initial = ''.join(word[0].upper() for word in name.split())
    initial = name.split()[0][0].upper() + name.split()[1][0].upper()
    if initial in initials:
        initials[initial].append(name)
    else:
        initials[initial] = [name]

print(initials)
#{'JD': ['John Doe', 'Jane Doe'], 'JJ': ['Jimmy Jimmy'], 'DJ': ['Door Jone']}

for i in range(int(q)):
    matches = initials.get(input())
    match matches:
        case None:
            print('nobody')
        case [a]:
            print(a)
        case [a, b]:
            print(a, b)
        case _:
            print('ambiguous')

#Note: google+claude3.5 assisted, but code handwritten