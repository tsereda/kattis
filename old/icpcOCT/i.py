import sys

def ok(n, x, y):
    return (0<=x<n and 0<=y<n)

def light(x, y, dx, dy):
   while ok(n, y+dy, x+dx) and (grid[y+dy][x+dx] == '.' or grid[y+dy][x+dx] == '!' or grid[y+dy][x+dx] == '?'):
        y += dy
        x += dx
        if grid[y][x] == '?':
            print(0)
            sys.exit(0)
        grid[y][x] = '!'

def adj(x,y):
    adjs = 0
    if(ok(n, x+1, y) and grid[y][x+1] == "?"): adjs += 1
    if(ok(n, x-1, y) and grid[y][x-1] == "?"): adjs += 1
    if(ok(n, x, y+1) and grid[y+1][x] == "?"): adjs += 1
    if(ok(n, x, y-1) and grid[y-1][x] == "?"): adjs += 1

    return adjs

n = int(input())

numboxes = []
grid = []

for _ in range(n):
   line = input()
   grid.append(list(line))

for y in range(n):
   for x in range(n):
       if (grid[y][x]=="?"):
            light(x,y,0,1)
            light(x,y,0,-1)
            light(x,y,1,0)
            light(x,y,-1,0)

for y in range(n):
   for x in range(n):
        if (grid[y][x].isdigit()):
            #print(f"{grid[y][x]} block at ({x},{y}) has {adj(x,y)} adjs")
            if int(grid[y][x]) != adj(x,y):
                print(0)
                sys.exit(0)

alllit=1
for y in range(n):
   for x in range(n):
       if (grid[y][x]=="."):
           alllit = 0

# for y in range(n):
#    print(grid[y])
print(alllit)