import string

p, t = map(int, input().split())

letters = {letter: [] for letter in string.ascii_uppercase[:p]}
# {'A': [], 'B': [], 'C': []
solves = []

for _ in range(t):
    teamname = input()
    letterschange = {}
    disolvedteams = []
    for letter in teamname:
        if letter in letters:
            #print(f"{1/len(teamname)}>{(1/(len(letters[letter])+10))}?")
            if(1/len(teamname))>(1/(len(letters[letter])+10)): #potential replacement
                letterschange[letter] = teamname
                print(f"disolving {letters[letter]}?")
                disolvedteams.append(letters[letter])

    #if each letter valid, apply change
    if len(letterschange) == len(teamname):
        for changedletter, value in letterschange.items():
            letters[changedletter] = value
        print(f"{teamname} applying {letterschange}")
        solves.append(teamname)
        for thing in disolvedteams:
            print(f"disolving {thing}")
            if thing in solves: solves.remove(thing)
    else:
        print(f"{teamname} invalid")

print(solves)
print(len(solves))