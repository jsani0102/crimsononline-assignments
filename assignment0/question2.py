import sys

def replace(str):
    length = len(str)
    letterCount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(length):
        if (ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')):
            letterCount[ord(str[i]) - ord('a')] += 1
    
    maxIndex = 0
    minIndex = 0
    maxOccurrences = 0
    minOccurrences = sys.maxint
    for i in range(26):
        if letterCount[i] > maxOccurrences:
            maxOccurrences = letterCount[i]
            maxIndex = i
        if letterCount[i] < minOccurrences and letterCount[i] != 0:
            minOccurrences = letterCount[i]
            minIndex = i
    maxChar = chr(maxIndex + ord('a'))
    minChar = chr(minIndex + ord('a'))

    s = list(str)
    for i in range(length):
        if s[i] == maxChar: s[i] = minChar
        elif s[i] == minChar: s[i] = maxChar
    
    print "".join(s)

string = "There were a lot of escopeoples in the elevator on Tuesday."

replace(string)
