def intput():
    return int(input())

n = intput()

for _ in range(n):
    #clean
    line = input()
    cleanedline = ""
    for i in range(len(line)):
        if line[i] in {'R', 'G', 'Y', 'B'}:
            cleanedline += line[i]

    if cleanedline[:5] != "YRRGR":
        print("eliminated")
        continue

    if cleanedline[-4:] != "RGRY":
        print("eliminated")
        continue

    #cheated on this line because I knew there was a better way than looping
    #count = cleanedline.count('G', cleanedline.find('Y'), cleanedline.rfind('Y'))

    #slighly more efficient
    Yseen = False
    Gseen = False
    Gs = 0
    for i in range(cleanedline.rfind('Y')):
        if cleanedline[i] == "Y":
            Yseen = True
        if Yseen and cleanedline[i] == "G":
            Gs += 1
        if cleanedline[i] == "G":
            Gseen = True
        if Gseen and cleanedline[i] == "G":
            secondG = i
    
    lastG = cleanedline.rfind('G')
    secondlastG = cleanedline[:lastG].rfind('G')
    
    if Gs%4 != 2:
        print("eliminated")
        continue

    #if Gs > 2 then between the second green and the second-last green Rs%3==0
    if cleanedline.count('R', secondG, secondlastG)%3== 0:
        print("eliminated")
        continue
    

    print("selected")