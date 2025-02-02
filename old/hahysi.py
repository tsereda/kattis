n, m = map(int, input().split())
MOD = 10**9 + 7

# Calculate number of ways to choose 2 rows and 2 columns
row_choices = (n * (n - 1)) // 2
col_choices = (m * (m - 1)) // 2

# Total combinations
total = (row_choices * col_choices) % MOD

print(total)