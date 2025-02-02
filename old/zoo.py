list_count = 1

while True:
    n = int(input())
    if n <= 0:
        break
    
    animals = {}
    for _ in range(n):
        last_word = input().split()[-1].lower()
        animals[last_word] = animals.get(last_word, 0) + 1
    
    print(f"List {list_count}:")
    for animal, count in sorted(animals.items()):
        print(f"{animal} | {count}")
    
    list_count += 1