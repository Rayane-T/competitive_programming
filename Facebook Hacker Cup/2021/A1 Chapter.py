with open('consistency_chapter_1_input.txt', 'r') as f:
    ft = f.readline()
    t = f.readlines()

S = "ABC"
S = list(S)

vowels = "AEIOU"
vowels = list(vowels)
consonents = "ZRTYPQSDFGHJKLMWXCVBN"
consonents = list(consonents)

def isVowel(c):
    if c in vowels:
        return True
def isConso(v):
    if v in consonents:
        return True

def max_occurence(S):
    count = 0
    max_index = 0
    for e in range(len(S)):
        count += 1
        S.count(S[e])
    return max_index

countV,countC,temps = 0,0,0

if len(S) == 1:
    print(temps)
else:
    for e in S:
        if isVowel(e):
            countV += 1
        elif isConso(e):
            countC += 1
    if countC >= countV:
        for x1 in range(len(S)):
            max_occ = max_occ(S)
            if isConso(S[x1]):
                S[x1] = consonents[0]
                temps += 1
            else:
                continue
    else:
        for x2 in range(len(S)):
            if isVowel(S[x2]):
                S[x2] = vowels[0]
                temps += 1
            else:
                temps += 1
                continue
    print(temps)
