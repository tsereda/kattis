k, q = map(int, input().split())

solvedproblems = {i: 0 for i in range(1, k+1)}

for _ in range(q):
    solvedproblems[int(input().split()[1])] += 1

print(min(solvedproblems.values()))