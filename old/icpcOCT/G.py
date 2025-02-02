n = int(input())

grid = []

for _ in range(n):
    print(n)
    line = input()
    grid.append(list(line))

for y in range(n):
    for x in range(n):
        #print(f"x:{x},y:{y},v:{grid[y][x]}")
        if (grid[y][x]=="?"):
            upblock = 0
            downblock = 0
            leftblock = 0
            rightblock = 0
            radius = 1
            #if there are unblock directions
            while not (upblock and downblock and leftblock and rightblock):
                if not upblock: 
                    try:
                        print(f"light ({x},{y}) trying to light up ({x},{y-radius}) (currently {grid[y-radius][x]})")
                        if grid[y+radius][x] == '.':
                            #! indicates a lit space
                            grid[y-radius][x] = '!'
                        else: upblock = 1
                    except:
                        upblock = 1

                    try:
                        print(f"light ({x},{y}) trying to light down ({x},{y+radius}) (currently {grid[y+radius][x]})")
                        if grid[y+radius][x] == '.':
                            #! indicates a lit space
                            grid[y+radius][x] = '!'
                        else: downblock = 1
                    except:
                        downblock = 1

                    try:
                        print(f"light ({x},{y}) trying to light left ({x+radius},{y}) (currently {grid[y][x+radius]})")
                        if grid[y][x+radius] == '.':
                            #! indicates a lit space
                            grid[y][x+radius] = '!'
                        else: leftblock = 1
                    except:
                        leftblock = 1

                    try:
                        print(f"light ({x},{y}) trying to light right ({x-radius},{y}) (currently {grid[y][x-radius]})")
                        if grid[y][x-radius] == '.':
                            #! indicates a lit space
                            grid[y][x-radius] = '!'
                        else: 
                            print("right blocked")
                            rightblock = 1
                    except:
                        print("right OOB")
                        rightblock = 1
                    radius+=1

for y in range(n):
    print(grid[y])