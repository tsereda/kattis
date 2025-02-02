n, r, c = input().split()

left = []

for _ in range(int(r)):
    left.append(input().split()[0])

for i in range(int(n)):
    name = input()
    if i%int(c)==0:
        #first name
        if name == left[i//int(c)]:
            print("left")
        else: 
            print("right")