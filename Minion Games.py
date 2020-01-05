def minion_game(string):
    # your code goes here
    i1 = 0
    i2 = 0
    Vowel_list = list ('AEIOU')
    for i in range (len(string)):
        if s[i] in Vowel_list:
            i1 += len(string)-i
        if s[i] not in Vowel_list:
            i2 += len(string)-i
    if i1 == i2:
        print('Draw')
    if i1 > i2:
        print('Kevin',i1)
    if i1 < i2:
        print('Stuart',i2)



#s = input()
s = 'BANANA'
minion_game(s)
