n, p, d = map(int, input().split())
pattern = input()

double_pattern = pattern + pattern

tired_count = 0

# Count Z's in initial window
sleep_count = double_pattern[:p].count('Z')

for i in range(n):
    # If sleep count in window is less than required, Terry is tired
    if sleep_count < d:
        tired_count += 1
    

print(tired_count)