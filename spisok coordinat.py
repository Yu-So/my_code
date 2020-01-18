# import itertools
# # from itertools import product
# #
# # list_1 = [('1' ,'2'), ('3', '4'), ('7', '8','9')]
# # list_2 = list(product(*list_1))
# # for i in list_2:
# #     print (i)
#
# print(ord('F'))
# print(chr(91))
#
# s = 'ABCDCDC'
# s1 = 'CDC'
#
# i = 0
# count = 0
# while i != -1:
#     j = s.find(s1[i:])
#     if j
#     print (i)

# width = 70
# string = 'Привет медведь !!!'
# print (string.ljust(width,'_'))
# print (string.rjust(width,'-'))
# print (string.center(width,'0'))
#
# print ('dsfsd'*3)
# import textwrap
# s = 'ABCDEFGHIJKLIMNOQRSTUVWXYtwretwrtwertwertwertwe'
# i = 5
# k = len(s) // i + 1
# print (k)
# #print (k)
# print(textwrap.fill(s,i))

# s = '123456789abcdef'
# print(s.center(17,'-'))

# number = 115
# w = len(bin(number)[2:])
#
# for i in range(1, number + 1):  #
#     print(str(int(i)).rjust(w, ' '), str(oct(i))[2:].rjust(w, ' '), str(hex(i))[2:].upper().rjust(w, ' '),
#           str(bin(i))[2:].rjust(w, ' '), sep=' ')

#a = list(range(15))
#print (a)


# s = 'jsdfl asjdasl 12weqo sadjal12'
# s1 = s.split(' ')
# print (s1)
# for i in s1:
#     print(i.capitalize(), end =' ')
#
# print(s1[:])

# a='ffewfqwefqwef'
# list_r = list(a)
# print('-'.join(list_r))
#
# print ('12345'[0])

# s = 'fdjslfsldfskdla'
# s1 = set (s)
# print (s1)
# s2 = ''.join(s1)
# print (s2)

# k = 2
# s = 'jldglkjsdflgjlsdfkjgl'
# for i in range (0,len(s),2):
#     print (s[i:i+2])

# list1 = {2,5,7,2,1}
# list2 = [2,5,7,1]
# print(list2)
# print(list2.sort())
# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# #print (Point)
# pt1 = Point(1,2)
# print(pt1.x)
# print(type(pt1))
# pt2 = Point(3,4)
# print(pt2)
#
# list1 = ['14','45','6']
# print(*int(list1))

# s = {23,31,213,432}
# s.pop()
# print(type(s))
# print(s)

# list1 = [i for i in range(6)]
# print (list1)
#r = [1,2,3,4,5]
# print('{} {} {}'.format(*r))
# print(r)
#
# [print(i) for i in range(5)]

# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# pt1 = Point(1,2)
# pt2 = Point(3,4)
# dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# print (dot_product)

#import collections
#c = collections.Counter('abracadabra')
#c = collections.Counter(a=15, b=2, c=0, d=-2)
#print(len(list(c.elements())))
#print(list(c))
#print(c.clear())

import collections
#import re

#c = collections.Counter('aabbddcce')
#print(c.most_common(4))

#l = re.search(r'a','caabbbbt')
#l = re.finditer(r'a','caabbbbt')
#for m in l:
#    print(m.span())

#print(re.search(r'a','caabbbbt').finditer())





#print(re.finditer(r'[a,t]','caabbbbt').next())

# mytuple = ("яблоко", "банан", "вишня")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))



#print(re.search(r'\d','f5').span[1])

# import re
# m = re.compile('aa')
# s = 'aaadaa'
#
# j=0
# m.search(s,j)
# flag = True
#
# while (m.search(s,j)):
#     match = m.search(s,j)
#     if match:
#         print(match.start())
#         j = match.start()+1
#     else:
#         flag = False
#
#
#     print('начинается = ', match.start())
#     # #print('кончается = ', match.end()-1)

# import re
#
# #Squaring numbers
# def square(match):
#     #number = int(match.group(0))
#     return '11'
#
# print (re.sub(r"aa", square, "aaadaa"))

import re

# html = """
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash"
#   data="your-file.swf"
#   width="0" height="0">
#   <!-- <param name="movie"  value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
# """

#print (re.sub("(<!--.*-->)", "", html)) #remove comment

#m = re.match(r'[789]{1}[0123456789]{2}', '895')
#print (m)

import re
#print(re.findall(r'[^0-9a-zA-Z]','ksd;sdf'))
#print(re.match(r'\d{16}$', '1234567891111234'))
#print(re.match(r'\d{4}-\d{4}-\d{4}-\d{4}$', '1234-5678-9111-1234'))
s = '5133-3327-8912-3456'
if not (re.match(r'[456]{1}\d{15}$', s) or re.match(r'[456]{1}\d{3}-\d{4}-\d{4}-\d{4}$', s)):
    #if not(re.match(r'\d{16}$', s) or re.match(r'\d{4}-\d{4}-\d{4}-\d{4}$', s)):
    print('не подходит')
else:
    print('подходит')
s = s.replace('-','')
print(s)

cnt = 1
flag = True
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        cnt += 1
        if cnt == 4:
            flag = False
            print('неверный номер карты')
    else:
        cnt = 1

print ('цифры')
s = '999999'
print (re.match(r'[1-9]{1}\d{5}$', s))

print('Кое что проверить ...')
def rtf(s):
    print (s)

rtf('1' if False else '2') # вызов функции с аргументом в зависимости от IF

print('Проверка регулярки .... _1_')  # использование или
print (re.search(r'a|b', 'cssssbc'))

print('Проверка регулярки .... _2_')  # Использование или
print (re.search(r'[abc]|[def]', 'gbu'))


print('Проверка вывода строки с префиксом -f- ')  # Использование или
s1 = 'Привет 1'
s2 = 'Привет 2'

print(f' Аргумент1 {s1} Аргумент2 {s2}') # печать строки, а внутри переменные

print('Проверка использования групп в функции re.sub')  # Использование или

text = '1b23'
print(re.sub(r'(\d)(b)',r'цифра \1 цифра b \2 b ', text))

print('Проверка использования групп при re.search()')  # Использование или

text = 'aabbbaa'
print(re.findall(r'(\w)\1', text))

print(' Комплексные числа ___ ')
l1 = [1,2]
x = complex(*l1)
print(x)



"""
Это коментарий?
"""

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print(X)

#print(re.macth(r'\d{16}$','12345678911112345'))

a = (23,12,34)
print(sum(a))

print(' --- Сортировка списка --- ')

a = [[5,4,3],[4,3,2],[3,2,1]]
#b = ['b','a','c']
print(a)
#print(b)
a.sort()
print (a)

print('123456789'[-5:])

print('Mr. Mike Thomson'.split())

print(map(int, ['123','23','12']))

print('Список --- ')
l = '44 55 11 15 4 72 26 91 80 14 43 78 70 75 36 83 78 91 17 17 54 65 60 21 58 98 87 45 75 97 81 18 51 43 84 54 66 10 44 45 23 38 22 44 65 9 78 42 100 94 58 5 11 69 26 20 19 64 64 93 60 96 10 10 39 94 15 4 3 10 1 77 48 74 20 12 83 97 5 82 43 15 86 5 35 63 24 53 27 87 45 38 34 7 48 24 100 14 80 54'.split()
print (l)
l.sort()
print (l)


l1 = l[0]
pairs = 0
i = 1
while i <= len(l) - 1:
    if l1 == l[i]:
        pairs += 1
        l1 = l[i + 1]
        i += 2
    else:
        l1 = l[i]
        i += 1
print(pairs)

print('Прогулка')

l = list('UDDDUDUU')

lev = 0
count = 0
startvalley = False
# finishvalley = False
for i in l:
    if i == 'U':
        lev += 1
        print('Вверх. Уровень ', lev)
    if i == 'D':
        lev -= 1
        print('Вниз. Уровень ', lev)

    if lev < 0 and startvalley == False:
        print('Зашел в ямку')
        count += 1
        startvalley = True
    if lev >= 0 and startvalley == True:
        print('Вышел из ямки')
        startvalley = False
print (count)




