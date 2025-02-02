n = int(input())

minv = 0
maxv = 99999999

for _ in range(n):
    minput, maxput = input().split()
    minv = max(minv, int(minput))
    maxv = min(maxv, int(maxput))

if minv <= maxv:
    print(maxv-minv+1, minv)
else:
    print('bad news')