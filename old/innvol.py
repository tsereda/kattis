#https://open.kattis.com/contests/sat25v/problems/innvols
input = input()
substrings = {}

for i in range(len(input)):
    for j in range(i+1, len(input)+1):
        substrings[input[i:j]] = input.count(input[i:j])
        
for substring, count in sorted(substrings.items(), key=lambda x: (-x[1], x[0])):
    print(f"{count} {substring}")

#claude3.5 helped with the key=lambda