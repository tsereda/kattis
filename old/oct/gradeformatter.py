from collections import deque

c, n = map(int, input().split())

errors = deque(input().split())

errorString = ""
correctString = ""

error = errors.popleft()
lastCorrect = False
start = end = 1

for i in range(1,c+1):  
    if str(i) == error:
        if not lastCorrect:
            end = i-1
            if start == end:
                correctString += f" {start}"
            if start < end:
                correctString += f" {start}-{end}"
            start = i
        
        if len(errors) > 0:
            error = errors.popleft() 
        lastCorrect=True
    else:
        if lastCorrect:      
            end = i-1
            if start == end:
                errorString += f" {end}"
            if start < end:
                errorString += f" {start}-{end}"
            start = i
        
        lastCorrect=False

if lastCorrect:
    if start == c:
        errorString += f" {c}"
    else:
        errorString += f" {start}-{c}"
else:
    if start == c:
        correctString += f" {c}"
    else:
        correctString += f" {start}-{c}"

# cheated on these rsplit lines
# Add commas between all items except last pair
errorString = errorString.rsplit(' ', 1)[0].replace(' ', ', ') + ' ' + ' '.join(errorString.rsplit(' ', 1)[1:])
correctString = correctString.rsplit(' ', 1)[0].replace(' ', ', ') + ' ' + ' '.join(correctString.rsplit(' ', 1)[1:])

# Add 'and'
errorString = errorString.rsplit(' ', 1)[0] + ' and ' + errorString.rsplit(' ', 1)[1]
correctString = correctString.rsplit(' ', 1)[0] + ' and ' + correctString.rsplit(' ', 1)[1]

print("Errors:" + errorString[1:])
print("Correct:" + correctString[1:])