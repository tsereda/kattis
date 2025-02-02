n = int(input())

positions = input().split(' ')

order = [1] * n
for i in range(1, n):
    order[int(positions[i-1])+1]=i+1
print(str(order))