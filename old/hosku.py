n = int(input())
#line
lines = []
for i in range(n):
    lines.append( [1] + input().split() )

for i in range(n):
    print(lines[i][int(lines[i][0])+1])
    if lines[i][0] == lines[i][1]:
        lines[i][0] += 1