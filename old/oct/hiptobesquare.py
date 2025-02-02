import math

n = int(input())

for _ in range(n):
    num = int(input())+1
    print((math.floor(math.sqrt(num))-1)//2)