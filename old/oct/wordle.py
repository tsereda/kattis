word = input()
guess = input()

output = ""
marked = []

for i in range(len(word)):
    if guess[i] == word[i]:
        output += "G"
        marked += guess[i]
    else:
        if guess[i] in word and guess[i] not in marked:
            output += "Y"
            marked += guess[i]
        else:
            output += "-"
print(output)